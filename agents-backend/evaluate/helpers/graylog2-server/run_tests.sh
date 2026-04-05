#!/bin/bash
set -e

WORKTREE_MODE="${WORKTREE_MODE:-0}"
SHORT_SHA="${COMMIT_SHA:-worktree}"
if [ "${WORKTREE_MODE}" != "1" ] && [ -n "${COMMIT_SHA:-}" ]; then
    SHORT_SHA="${COMMIT_SHA:0:7}"
fi

echo "=== Running Tests for ${SHORT_SHA} ==="
echo "Targets: ${TEST_TARGETS:-}"

MAX_CPU="${MAX_CPU:-$(getconf _NPROCESSORS_ONLN 2>/dev/null || nproc 2>/dev/null || echo 1)}"
MAVEN_THREADS="${MAVEN_THREADS:-${MAX_CPU}}"
SUREFIRE_FORKS="${SUREFIRE_FORKS:-${MAX_CPU}}"

echo "CPU detected: ${MAX_CPU}"
echo "Maven threads: ${MAVEN_THREADS}"
echo "Surefire forks: ${SUREFIRE_FORKS}"

# 1. Configure Test Command
if [ "${TEST_TARGETS:-}" == "ALL" ]; then
    # Run unit tests for everything
    MAVEN_ARGS=""
elif [ "${TEST_TARGETS:-}" == "NONE" ]; then
    echo "No relevant source code changes found. Skipping tests."
    exit 0
else
    # TEST_TARGETS is a space-separated list of "module:class"
    
    MODULES=""
    TESTS=""
    
    # Split by space
    for target in ${TEST_TARGETS}; do
        # Split by colon
        mod="${target%%:*}"
        cls="${target#*:}"
        
        # Append to lists (comma separated)
        if [ -z "$MODULES" ]; then
            MODULES="$mod"
        else
            # Avoid duplicates in modules list
            if [[ ",$MODULES," != *",$mod,"* ]]; then
                MODULES="$MODULES,$mod"
            fi
        fi
        
        if [ -z "$TESTS" ]; then
            TESTS="$cls"
        else
            TESTS="$TESTS,$cls"
        fi
    done
    
    MAVEN_ARGS="-pl ${MODULES} -Dtest=${TESTS} -am"
fi

echo "--- Starting Test Execution ---"
echo "--- Command: mvn test ${MAVEN_ARGS} ---"

# 2. Run Tests
docker volume create maven-repo 2>/dev/null || true

# Get Docker group ID from host
DOCKER_GID=$(stat -c '%g' /var/run/docker.sock 2>/dev/null || echo 0)

# BUILDER_IMAGE_TAG is the primary tag, IMAGE_TAG is the fallback
IMAGE_TAG="${BUILDER_IMAGE_TAG:-${IMAGE_TAG}}"

if docker run --rm \
    --privileged \
    -v "${PROJECT_DIR}:/repo" \
    -v "maven-repo:/root/.m2/repository" \
    -v "/var/run/docker.sock:/var/run/docker.sock" \
    -e TESTCONTAINERS_RYUK_DISABLED=true \
    -e TESTCONTAINERS_CHECKS_DISABLE=true \
    -e DOCKER_HOST=unix:///var/run/docker.sock \
    --group-add "${DOCKER_GID}" \
    -w /repo \
    "${IMAGE_TAG}" \
    bash -c "chmod 666 /var/run/docker.sock 2>/dev/null || true; \
             if [ \"${WORKTREE_MODE}\" != \"1\" ]; then git checkout -f ${COMMIT_SHA}; fi; \
             export MAVEN_OPTS='-Xmx4g -Xms2g -XX:ActiveProcessorCount=${MAX_CPU}'; \
             mvn clean test ${MAVEN_ARGS} -T ${MAVEN_THREADS} -DforkCount=${SUREFIRE_FORKS} -DreuseForks=true -Dmaven.compile.fork=true -Dswagger.skip=true -DfailIfNoTests=false -Denforcer.skip=true -Dskip.yarn -Dskip.npm -Dskip.installnodenpm -Dmaven.antrun.skip=true -Dmaven.javadoc.skip=true -Dcheckstyle.skip=true -Dforbiddenapis.skip=true -Dpmd.skip=true -Drat.skip=true -Dspotbugs.skip=true -Djacoco.skip=true; \
             MVN_EXIT_CODE=\$?; \
             mkdir -p /repo/build/all-test-results; \
             find . -name 'TEST-*.xml' -exec cp {} /repo/build/all-test-results/ \;; \
             exit \$MVN_EXIT_CODE"; then
    
    echo "✅ Tests Passed"
    exit 0
else
    echo "❌ Tests Failed"
    exit 1
fi