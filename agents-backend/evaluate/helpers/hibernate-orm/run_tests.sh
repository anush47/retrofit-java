#!/bin/bash
set -e

echo "=== Running Tests for ${COMMIT_SHA:0:7} ==="
echo "Target: ${TEST_TARGETS}"

IMAGE_TAG="${IMAGE_TAG:-hibernate-orm-builder:local}"

if [ "${TEST_TARGETS}" == "ALL" ]; then
    GRADLE_CMD="./gradlew test --rerun-tasks"
elif [ "${TEST_TARGETS}" == "NONE" ]; then
    echo "No relevant source code changes found. Skipping tests."
    exit 0
else
    # TEST_TARGETS is a space-separated list of "module:class"
    GRADLE_CMD_LIST=""
    for item in $TEST_TARGETS; do
        if [[ $item == *":"* ]]; then
            # Format: module:class
            mod="${item%%:*}"
            cls="${item#*:}"
            
            # If mod is empty, try to find it by searching for the class file
            if [[ -z "$mod" ]]; then
                echo "DEBUG: mod was empty for $item, searching for module..."
                # Find the class and extract the first part of the path
                class_rel_path=$(find . -name "${cls##*.}".java -o -name "${cls##*.}".kt | grep -v "/build/" | head -n 1 | sed 's|^./||')
                if [[ -n "$class_rel_path" ]]; then
                    mod="${class_rel_path%%/*}"
                    echo "DEBUG: Found module $mod for $cls"
                fi
            fi

            # Ensure module is prefixed with : if it's NOT the root project
            if [[ -n "$mod" ]]; then
                MODULE_PREFIX=":${mod}"
            else
                MODULE_PREFIX=""
            fi
            GRADLE_ARGS="${MODULE_PREFIX}:test --tests ${cls}"
        else
            # Format: class-only? Or something else. Hibernate targets module:class
            # Fallback to rooting at the project level
            GRADLE_ARGS=":test --tests ${item}"
        fi
        GRADLE_CMD_LIST="${GRADLE_CMD_LIST} ${GRADLE_ARGS}"
    done
    GRADLE_CMD="./gradlew ${GRADLE_CMD_LIST} --rerun-tasks"
fi

DOCKER_CMD="docker"
${DOCKER_CMD} volume create gradle-cache-hibernate 2>/dev/null || true
${DOCKER_CMD} volume create gradle-wrapper-hibernate 2>/dev/null || true

run_gradle_tests() {
    local extra_setup="$1"
    
    # We use -i for info logs to help helpful console parsing if XMLs are missing
    docker run --rm \
    -v "${PROJECT_DIR}:/repo" \
    -v "gradle-cache-hibernate:/home/gradle/.gradle/caches" \
    -v "gradle-wrapper-hibernate:/home/gradle/.gradle/wrapper" \
    -w /repo \
    "${IMAGE_TAG}" \
    bash -c "set -e; \
    ${extra_setup} \
    git config --global --add safe.directory /repo; \
    ${GRADLE_CMD} -i; \
    RET=\$?; \
    exit \$RET"
}

echo "--- Executing tests with default JDK ---"
if run_gradle_tests "" > test_output.log 2>&1; then
    cat test_output.log
    echo "✅ Tests Passed"
    exit 0
fi

cat test_output.log

# Check for known JDK version issues
if grep -q "requires at least JDK 25" test_output.log || grep -q "Unsupported class file major version 69" test_output.log; then
    echo "--- Detected JDK 25 requirement. Retrying tests with JDK 25... ---"
    SETUP_JDK25="export JAVA_HOME=/opt/java/jdk-25; export PATH=\$JAVA_HOME/bin:\$PATH;"
    
    if run_gradle_tests "${SETUP_JDK25}" > test_output.log 2>&1; then
        cat test_output.log
        echo "✅ Tests Passed"
        exit 0
    fi
    cat test_output.log
fi

echo "❌ Tests Failed"
exit 1