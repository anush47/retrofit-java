package com.retrofit.analysis.mcp;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
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
    private final ObjectMapper objectMapper;
    private final Map<String, SseEmitter> emitters = new ConcurrentHashMap<>();
    private final ExecutorService executor = Executors.newCachedThreadPool();

    public McpServer(GetJavaVersionTool getJavaVersionTool, ObjectMapper objectMapper) {
        this.getJavaVersionTool = getJavaVersionTool;
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

    @PostMapping("/messages")
    public void handleMessage(@RequestParam String sessionId, @RequestBody JsonNode request) {
        SseEmitter emitter = emitters.get(sessionId);
        if (emitter == null) {
            System.out.println("Session not found for message: " + sessionId);
            throw new IllegalArgumentException("Session not found: " + sessionId);
        }

        executor.submit(() -> {
            try {
                handleRequest(sessionId, request, emitter);
            } catch (Exception e) {
                System.out.println("Error handling request for " + sessionId + ": " + e.getMessage());
                e.printStackTrace();
            }
        });
    }

    private void handleRequest(String sessionId, JsonNode request, SseEmitter emitter) throws Exception {
        if (!request.has("id")) {
            System.out.println("Received notification [" + sessionId + "]");
            return;
        }

        JsonNode idNode = request.get("id");
        String id = idNode.asText();
        String method = request.get("method").asText();

        System.out.println("Received request [" + sessionId + "]: " + method + " (id: " + id + ")");

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
            var tool = tools.addObject();
            tool.put("name", "get_java_version");
            tool.put("description", "Returns the Java version of the analysis engine");
            tool.putObject("inputSchema").put("type", "object");
        } else if ("tools/call".equals(method)) {
            JsonNode params = request.get("params");
            String name = params.get("name").asText();
            if ("get_java_version".equals(name)) {
                ObjectNode result = response.putObject("result");
                var contentArray = result.putArray("content");
                var textContent = contentArray.addObject();
                textContent.put("type", "text");
                textContent.put("text", getJavaVersionTool.execute());
            } else {
                ObjectNode error = response.putObject("error");
                error.put("code", -32601);
                error.put("message", "Method not found: " + name);
            }
        } else {
            System.out.println("Unknown method: " + method);
            // Ignore unknown methods
        }

        // Send response via SSE
        String responseString = objectMapper.writeValueAsString(response);
        System.out.println("Sending response [" + sessionId + "] for id " + id);
        try {
            emitter.send(SseEmitter.event().name("message").data(responseString));
            System.out.println("Response sent successfully.");
        } catch (Exception e) {
            System.out.println("Failed to send response: " + e.getMessage());
            throw e;
        }
    }
}
