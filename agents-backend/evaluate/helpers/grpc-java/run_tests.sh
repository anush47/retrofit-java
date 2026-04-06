#!/bin/bash
# Runs targeted grpc-java tests inside Docker.
set -e

echo "=== Running grpc-java Tests for ${COMMIT_SHA:0:7} ==="
echo "Target: ${TEST_TARGETS}"

HOST_UID="${HOST_UID:-$(id -u)}"
HOST_GID="${HOST_GID:-$(id -g)}"
echo "--- Container user: ${HOST_UID}:${HOST_GID} ---"

IMAGE_TAG="${IMAGE_TAG:-retrofit-grpc-java-builder:local}"
MAX_CPU="${MAX_CPU:-$(getconf _NPROCESSORS_ONLN 2>/dev/null || nproc 2>/dev/null || echo 1)}"
echo "CPU detected: ${MAX_CPU}"

# 1. Determine Gradle test command from TEST_TARGETS.
# TEST_TARGETS is expected to be a space-separated string of '--tests "ClassName"'.
if [ "${TEST_TARGETS:-}" == "ALL" ]; then
    GRADLE_ARGS="test -PskipAndroid=true -x :grpc-compiler:compileJava_pluginExecutableJava_pluginCpp"
elif [ -n "${TEST_TARGETS:-}" ] && [ "${TEST_TARGETS}" != "NONE" ]; then
    GRADLE_ARGS="test ${TEST_TARGETS} -PskipAndroid=true -x :grpc-compiler:compileJava_pluginExecutableJava_pluginCpp"
else
    echo "No relevant test targets. Skipping tests."
    exit 0
fi

# Determine Docker command (with or without sudo).
DOCKER_CMD="docker"
if ! docker info > /dev/null 2>&1; then
    if sudo docker info > /dev/null 2>&1; then
        echo "Docker requires sudo. Using 'sudo docker'."
        DOCKER_CMD="sudo docker"
    fi
fi

echo "--- Setting cache permissions ---"
${DOCKER_CMD} run --rm -u root \
    -v "gradle-cache-grpc-java:/home/gradle/.gradle/caches" \
    -v "gradle-wrapper-grpc-java:/home/gradle/.gradle/wrapper" \
    "${IMAGE_TAG}" \
    chown -R "${HOST_UID}:${HOST_GID}" /home/gradle/.gradle

GRADLE_CMD="./gradlew ${GRADLE_ARGS} --max-workers=${MAX_CPU} --no-daemon"
echo "--- Executing: ${GRADLE_CMD} ---"

set +e
${DOCKER_CMD} run --rm \
    --dns=8.8.8.8 \
    -e HOME=/tmp \
    -e XDG_CONFIG_HOME=/tmp \
    -u "${HOST_UID}:${HOST_GID}" \
    -v "gradle-cache-grpc-java:/home/gradle/.gradle/caches" \
    -v "gradle-wrapper-grpc-java:/home/gradle/.gradle/wrapper" \
    -v "${PROJECT_DIR}:/repo" \
    -w /repo \
    "${IMAGE_TAG}" \
    bash -c "git config --global --add safe.directory /repo || true; \
    export GRADLE_OPTS=\"\${GRADLE_OPTS:-} -XX:ActiveProcessorCount=${MAX_CPU} -Xmx2g\"; \
    ${GRADLE_CMD}; \
    GRADLE_EXIT=\$?; \
    echo \"--- Tests finished with exit code \$GRADLE_EXIT ---\"; \
    exit \$GRADLE_EXIT"
EXIT_CODE=$?
set -e

exit ${EXIT_CODE}