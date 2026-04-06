# Validation Trace

## Blueprint Summary
- **Root Cause**: Deterministic inference: target branch diverges from mainline; adapt hunks with exact target context.
- **Fix Logic**: Apply each source hunk with target-verified context and symbol consistency while preserving behavior.
- **Dependent APIs**: ['indexed', 'encodeFlattenedToken', 'path', 'NodeFeature']

## Hunk Segregation
- Code files: 7
- Test files: 0
- Developer auxiliary hunks: 19

## Agent Tool Steps

  - `Agent calls apply_adapted_hunks` with `{"code_count": 4, "developer_aux_count": 19, "effective_code_count": 23, "test_count": 0}`
  - `Tool: apply_adapted_hunks` -> {'success': True, 'output': 'All hunks applied successfully.', 'applied_files': ['server/src/main/java/org/elasticsearch/index/mapper/DocumentParser.java', 'server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java', 'server/src/main/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapper.java', 'server/src/main/java/org/elasticsearch/index/mapper/MapperFeatures.java', 'docs/changelog/113910.yaml', 'rest-api-spec/src/yamlRestTest/resources/rest-api-spec/test/indices.create/20_synthetic_source.yml', 'server/src/test/java/org/elasticsearch/index/mapper/IgnoredSourceFieldMapperTests.java']}
  - `Agent calls run_build_script` with `{}`
  - `Tool: run_build_script` -> {'success': False, 'output': '--- Building Elasticsearch for faaf4ba ---\n--- Container user: 1000:1000 ---\nCPU detected: 16\n--- Changing directory to /home/cseroot/retrofit-java/temp_repo_storage/elasticsearch ---\ngradle-cache-es\ngradle-wrapper-es\n--- Building Docker image: retrofit-elasticsearch-builder:local ---\nSending build context to Docker daemon  23.04kB\n\nStep 1/8 : FROM eclipse-temurin:21-jdk-jammy\n ---> 6f2cc16588c8\nStep 2/8 : RUN apt-get update && apt-get install -y     git     rsync     && rm -rf /var/lib/apt/lists/*\n ---> Using cache\n ---> e108a380f3fe\nStep 3/8 : RUN groupadd --gid 1000 gradle &&     useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home gradle\n ---> Using cache\n ---> b2ea64ddb2fe\nStep 4/8 : RUN mkdir -p /home/gradle/.gradle &&     chown -R gradle:gradle /home/gradle/.gradle\n ---> Using cache\n ---> 3979f3c8607f\nStep 5/8 : RUN echo "org.gradle.daemon=false" >> /home/gradle/.gradle/gradle.properties &&     echo "org.gradle.parallel=... [TRUNCATED]

**Final Status: BUILD FAILED**

**Agent Analysis:**
API/signature mismatch in generated patch against target branch. Compiler errors: /repo/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java:350: error: cannot find symbol | /repo/server/src/main/java/org/elasticsearch/index/mapper/DocumentParserContext.java:353: error: cannot find symbol