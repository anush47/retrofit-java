package com.retrofit.analysis.tools;

import org.springframework.stereotype.Component;
import spoon.Launcher;
import spoon.reflect.declaration.CtType;
import spoon.reflect.reference.CtTypeReference;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Component
public class GetHierarchyTool {

    public Map<String, Object> execute(String targetRepoPath, String className) {
        Launcher launcher = new Launcher();
        // We add the target repo path as source
        launcher.addInputResource(targetRepoPath);

        // Configure Spoon to be lenient with missing classpath (since we might not have
        // all deps built)
        launcher.getEnvironment().setNoClasspath(true);
        launcher.getEnvironment().setCommentEnabled(false); // We don't need comments for hierarchy

        try {
            launcher.buildModel();
        } catch (Exception e) {
            Map<String, Object> error = new HashMap<>();
            error.put("error", "Failed to build model: " + e.getMessage());
            return error;
        }

        CtType<?> type = launcher.getFactory().Type().get(className);

        Map<String, Object> result = new HashMap<>();
        result.put("className", className);

        if (type == null) {
            result.put("found", false);
            result.put("message", "Class not found in the provided path.");
            return result;
        }

        result.put("found", true);

        // Superclass
        CtTypeReference<?> superClass = type.getSuperclass();
        if (superClass != null) {
            result.put("superclass", superClass.getQualifiedName());
        } else {
            result.put("superclass", "java.lang.Object"); // Default
        }

        // Interfaces
        List<String> interfaces = new ArrayList<>();
        for (CtTypeReference<?> iface : type.getSuperInterfaces()) {
            interfaces.add(iface.getQualifiedName());
        }
        result.put("interfaces", interfaces);

        // Also get fields and methods for context?
        // For now, let's keep it strictly hierarchy.

        return result;
    }
}
