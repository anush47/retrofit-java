#!/bin/bash
# This script compiles HBase code using pre-built Docker image (Maven project)
set -e # Exit on error

WORKTREE_MODE="${WORKTREE_MODE:-0}"
echo "--- Building HBase for commit ${COMMIT_SHA:0:7} --- (WORKTREE_MODE=${WORKTREE_MODE})"

echo "--- Changing directory to ${PROJECT_DIR} ---"
cd "${PROJECT_DIR}"

if [ "${WORKTREE_MODE}" != "1" ]; then
    echo "--- Checking out commit... ---"
    git checkout -f ${COMMIT_SHA}
fi

# 2. Build Docker image
echo "--- Building Docker image... ---"
# Use TOOLKIT_DIR as context to avoid permission errors in target/ folders
docker build -t ${BUILDER_IMAGE_TAG} -f ${TOOLKIT_DIR}/Dockerfile ${TOOLKIT_DIR}

# 3. Create persistent Maven cache volume
docker volume create maven-cache-hbase 2>/dev/null || true

echo "--- Running Maven build (compile only, no tests) ---"

# Build without tests, skip documentation and code quality checks
BUILD_COMMAND="mvn clean install -DskipTests \
  -Dmaven.javadoc.skip=true \
  -Dcheckstyle.skip=true \
  -Dfindbugs.skip=true \
  -Dspotbugs.skip=true \
  -Denforcer.skip=true"

if docker run --rm \
    --dns=8.8.8.8 \
    -v "${PROJECT_DIR}:/repo" \
    -v "maven-cache-hbase:/root/.m2" \
    -w /repo \
    ${BUILDER_IMAGE_TAG} \
    bash -c "rm -rf /root/.m2/repository/org/apache/hbase && ${BUILD_COMMAND}"; then
    BUILD_EXIT_CODE=0
else
    BUILD_EXIT_CODE=1
fi

# Save build status
if [ -n "${BUILD_STATUS_FILE:-}" ]; then
    if [ "${BUILD_EXIT_CODE}" -eq 0 ]; then
        echo "Success" > "${BUILD_STATUS_FILE}"
    else
        echo "Fail" > "${BUILD_STATUS_FILE}"
    fi
fi

echo "--- Build complete for ${COMMIT_SHA:0:7} ---"
exit ${BUILD_EXIT_CODE}
