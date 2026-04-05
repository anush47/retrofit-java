#!/bin/bash
set -e

WORKTREE_MODE="${WORKTREE_MODE:-0}"
SHORT_SHA="${COMMIT_SHA:-worktree}"
if [ "${WORKTREE_MODE}" != "1" ] && [ -n "${COMMIT_SHA:-}" ]; then
    SHORT_SHA="${COMMIT_SHA:0:7}"
fi

echo "=== Building Graylog for ${SHORT_SHA} ==="

MAX_CPU="${MAX_CPU:-$(getconf _NPROCESSORS_ONLN 2>/dev/null || nproc 2>/dev/null || echo 1)}"
MAVEN_THREADS="${MAVEN_THREADS:-${MAX_CPU}}"

echo "CPU detected: ${MAX_CPU}"
echo "Maven threads: ${MAVEN_THREADS}"

cd "${PROJECT_DIR}"

if [ "${WORKTREE_MODE}" != "1" ]; then
    echo "--- Checking out commit ${COMMIT_SHA}... ---"
    git checkout -f ${COMMIT_SHA}
fi

# 2. Build Docker image
echo "--- Building Docker image... ---"
IMAGE_TAG="${BUILDER_IMAGE_TAG:-${IMAGE_TAG}}"
docker build -t ${IMAGE_TAG} -f ${TOOLKIT_DIR}/Dockerfile ${TOOLKIT_DIR}

# 3. Run Build
echo "--- Running Maven Build... ---"

# Create volume for maven repo if not exists
docker volume create maven-repo 2>/dev/null || true

# Run build
if docker run --rm \
    -v "${PROJECT_DIR}:/repo" \
    -v "maven-repo:/root/.m2/repository" \
    -w /repo \
    ${IMAGE_TAG} \
    bash -c "export MAVEN_OPTS='-Xmx4g -Xms2g -XX:ActiveProcessorCount=${MAX_CPU}'; mvn clean install -DskipTests -Dskip.yarn -Dskip.npm -Dskip.installnodenpm -Dmaven.antrun.skip=true -Dmaven.javadoc.skip=true -Dcheckstyle.skip=true -Dpmd.skip=true -Dforbiddenapis.skip=true -Denforcer.skip=true -Drat.skip=true -Dspotbugs.skip=true -Djacoco.skip=true -Dswagger.skip=true -Dmaven.source.skip=true -T ${MAVEN_THREADS}"; then
    
    if [ -n "${BUILD_STATUS_FILE:-}" ]; then
        echo "Success" > "${BUILD_STATUS_FILE}" || true
    fi
    echo "✅ Build succeeded for ${SHORT_SHA}"
else
    if [ -n "${BUILD_STATUS_FILE:-}" ]; then
        echo "Fail" > "${BUILD_STATUS_FILE}" || true
    fi
    echo "❌ Build failed for ${SHORT_SHA}"
    exit 1
fi

echo "--- Build complete for ${SHORT_SHA} ---"