#!/bin/bash
set -e

WORKTREE_MODE="${WORKTREE_MODE:-0}"
echo "=== Running Tests for ${COMMIT_SHA:0:7} === (WORKTREE_MODE=${WORKTREE_MODE})"
echo "Target: ${TEST_TARGETS}"

# 1. Configure Test Command
if [ "${TEST_TARGETS}" == "ALL" ]; then
    echo "--- Running ALL tests (excluding blacklisted modules) ---"
    MAVEN_ARGS="-pl '!hbase-assembly,!hbase-archetypes'"
elif [ "${TEST_TARGETS}" == "NONE" ]; then
    echo "No relevant source code changes found. Skipping tests."
    exit 0
else
    # Check if we have granular targets (contain ':')
    if [[ "${TEST_TARGETS}" == *":"* ]]; then
        echo "--- Granular Test Mode: Running specific test classes ---"
        
        MODULES=""
        CLASSES=""
        
        # Parse targets
        for target in ${TEST_TARGETS}; do
            if [[ "$target" == *":"* ]]; then
                MOD="${target%%:*}"
                CLS="${target#*:}"
                
                # Add to comma-separated lists
                if [ -z "$MODULES" ]; then
                    MODULES="$MOD"
                else
                    # Check if module already in list
                    if [[ ",$MODULES," != *",$MOD,"* ]]; then
                        MODULES="$MODULES,$MOD"
                    fi
                fi
                
                if [ -z "$CLASSES" ]; then
                    CLASSES="$CLS"
                else
                    CLASSES="$CLASSES,$CLS"
                fi
            fi
        done
        
        if [ -z "$CLASSES" ]; then
            echo "Error: No valid test classes found"
            exit 1
        fi
        
        echo "Modules: $MODULES"
        echo "Test Classes: $CLASSES"
        echo "Number of test classes: $(echo $CLASSES | tr ',' '\n' | wc -l)"
        
        # Use -Dtest and -Dit.test, -am to build dependencies
        MAVEN_ARGS="-pl ${MODULES} -Dtest=${CLASSES} -Dit.test=${CLASSES} -am -DfailIfNoTests=false"
    else
        echo "--- Module Test Mode: Running all tests in affected modules ---"
        
        # Convert space-separated to comma-separated
        COMMA_TARGETS=$(echo "${TEST_TARGETS}" | tr ' ' ',')
        
        echo "Affected Modules: $COMMA_TARGETS"
        
        # Run all tests in specified modules, build dependencies
        MAVEN_ARGS="-pl ${COMMA_TARGETS} -am"
    fi
fi

echo "--- Starting Test Execution ---"
echo "--- Maven Args: ${MAVEN_ARGS} ---"

# 2. Create Maven cache volume
docker volume create maven-cache-hbase 2>/dev/null || true

# 3. Run Tests in Docker
CHECKOUT_CMD="git checkout -f ${COMMIT_SHA}"
if [ "${WORKTREE_MODE}" == "1" ]; then
    CHECKOUT_CMD="echo 'Skipping checkout (WORKTREE_MODE=1)'"
fi

if docker run --rm \
    --dns=8.8.8.8 \
    -v "${PROJECT_DIR}:/repo" \
    -v "maven-cache-hbase:/root/.m2" \
    -w /repo \
    "${BUILDER_IMAGE_TAG}" \
    bash -c "set -e; \
             echo 'Maven version:'; mvn --version; \
             ${CHECKOUT_CMD}; \
             echo 'Running: mvn verify ${MAVEN_ARGS}'; \
             mvn verify ${MAVEN_ARGS} \
                 -DfailIfNoTests=false \
                 -Dmaven.javadoc.skip=true \
                 -Dcheckstyle.skip=true \
                 -Dfindbugs.skip=true \
                 -Dspotbugs.skip=true \
                 -Denforcer.skip=true; \
             MVN_EXIT_CODE=$?; \
             echo 'Collecting test results...'; \
             mkdir -p /repo/target/all-test-results; \
             find . -type f \( -path '*/target/surefire-reports/*.xml' -o -path '*/target/failsafe-reports/*.xml' \) -not -path '*/target/all-test-results/*' -exec cp {} /repo/target/all-test-results/ \; 2>/dev/null || true; \
             echo "Found $(ls /repo/target/all-test-results/*.xml 2>/dev/null | wc -l) test result files"; \
             exit $MVN_EXIT_CODE"; then
    
    echo "✅ Tests Passed"
    exit 0
else
    echo "❌ Tests Failed"
    exit 1
fi
