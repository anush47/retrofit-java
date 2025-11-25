package com.retrofit.analysis.mcp;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.retrofit.analysis.tools.GetHierarchyTool;
import com.retrofit.analysis.tools.GetJavaVersionTool;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@RestController
@RequestMapping("/mcp")
public class McpServer {

    private final GetJavaVersionTool getJavaVersionTool;
    private final GetHierarchyTool getHierarchyTool;
    private final ObjectMapper objectMapper;
    private final Map<String, SseEmitter> emitters = new ConcurrentHashMap<>();
    private final ExecutorService executor = Executors.newCachedThreadPool();

    public McpServer(GetJavaVersionTool getJavaVersionTool, GetHierarchyTool getHierarchyTool,
            ObjectMapper objectMapper) {
        this.getJavaVersionTool = getJavaVersionTool;
        this.getHierarchyTool = getHierarchyTool;
        this.objectMapper = objectMapper;
    }

    @GetMapping(value = "/sse", produces = org.springframework.http.MediaType.TEXT_EVENT_STREAM_VALUE)
    public SseEmitter handleSse() {
        SseEmitter emitter = new SseEmitter(Long.MAX_VALUE);
        String id = java.util.UUID.randomUUID().toString();
        emitters.put(id, emitter);

        System.out.println("SSE Connection initiated: " + id);

        emitter.onCompletion(() -> {
            System.out.println("SSE Completed: " + id);
            emitters.remove(id);
        });
        emitter.onTimeout(() -> {
            System.out.println("SSE Timeout: " + id);
            emitters.remove(id);
        });
        emitter.onError((e) -> {
            System.out.println("SSE Error [" + id + "]: " + e.getMessage());
            emitters.remove(id);
        });

        executor.submit(() -> {
            try {
                // Wait a bit to ensure connection is established
                Thread.sleep(500);
                String endpointUri = "/mcp/messages?sessionId=" + id;
                System.out.println("Sending endpoint event to " + id + ": " + endpointUri);
                emitter.send(SseEmitter.event().name("endpoint").data(endpointUri));
            } catch (Exception e) {
                System.out.println("Error sending endpoint event to " + id + ": " + e.getMessage());
                emitters.remove(id);
            }
        });

        return emitter;
    }

    @PostMapping("/sync/call")
    public JsonNode handleSyncCall(@RequestBody JsonNode request) {
        System.out.println("Received SYNC request");
        return processRequest(request);
    }

    @PostMapping("/messages")
    public void handleMessage(@RequestParam String sessionId, @RequestBody JsonNode request) {
        SseEmitter emitter = emitters.get(sessionId);
        if (emitter == null) {
            System.out.println("Session not found for message: " + sessionId);
            throw new IllegalArgumentException("Session not found: " + sessionId);
        }

        executor.submit(() -> {
            try {
                JsonNode response = processRequest(request);
                // Send response via SSE
                String responseString = objectMapper.writeValueAsString(response);
                System.out.println("Sending response [" + sessionId + "]");
                emitter.send(SseEmitter.event().name("message").data(responseString));
            } catch (Exception e) {
                System.out.println("Error handling request for " + sessionId + ": " + e.getMessage());
                e.printStackTrace();
            }
        });
    }

    private ObjectNode processRequest(JsonNode request) {
        if (!request.has("id")) {
            System.out.println("Received notification (ignoring for sync)");
            return objectMapper.createObjectNode();
        }

        JsonNode idNode = request.get("id");
        String method = request.get("method").asText();

        ObjectNode response = objectMapper.createObjectNode();
        response.put("jsonrpc", "2.0");
        response.set("id", idNode);

        if ("initialize".equals(method)) {
            ObjectNode result = response.putObject("result");
            result.put("protocolVersion", "2024-11-05");
            ObjectNode capabilities = result.putObject("capabilities");
            capabilities.putObject("tools");
            ObjectNode serverInfo = result.putObject("serverInfo");
            serverInfo.put("name", "analysis-engine");
            serverInfo.put("version", "0.1.0");
        } else if ("tools/list".equals(method)) {
            ObjectNode result = response.putObject("result");
            var tools = result.putArray("tools");

            var tool1 = tools.addObject();
            tool1.put("name", "get_java_version");
            tool1.put("description", "Returns the Java version of the analysis engine");
            tool1.putObject("inputSchema").put("type", "object");

            var tool2 = tools.addObject();
            tool2.put("name", "get_type_hierarchy");
            tool2.put("description", "Returns the type hierarchy (superclass, interfaces) of a given class");
            var inputSchema = tool2.putObject("inputSchema");
            inputSchema.put("type", "object");
            var properties = inputSchema.putObject("properties");
            properties.putObject("target_repo_path").put("type", "string");
            properties.putObject("class_name").put("type", "string");
            var required = inputSchema.putArray("required");
            required.add("target_repo_path");
            required.add("class_name");

        } else if ("tools/call".equals(method)) {
            JsonNode params = request.get("params");
            String name = params.get("name").asText();
            JsonNode args = params.get("arguments");

            if ("get_java_version".equals(name)) {
                ObjectNode result = response.putObject("result");
                var contentArray = result.putArray("content");
                var textContent = contentArray.addObject();
                textContent.put("type", "text");
                textContent.put("text", getJavaVersionTool.execute());
            } else if ("get_type_hierarchy".equals(name)) {
                String targetRepoPath = args.get("target_repo_path").asText();
                String className = args.get("class_name").asText();

                Map<String, Object> hierarchy = getHierarchyTool.execute(targetRepoPath, className);

                try {
                    ObjectNode result = response.putObject("result");
                    var contentArray = result.putArray("content");
                    var textContent = contentArray.addObject();
                    textContent.put("type", "text");
                    String jsonString = objectMapper.writeValueAsString(hierarchy);
                    textContent.put("text", jsonString);
                } catch (Exception e) {
                    ObjectNode error = response.putObject("error");
                    error.put("code", -32603);
                    error.put("message", "Internal error: " + e.getMessage());
                }
            } else {
                ObjectNode error = response.putObject("error");
                error.put("code", -32601);
                error.put("message", "Method not found: " + name);
            }
        } else {
            System.out.println("Unknown method: " + method);
        }

        return response;
    }
}
