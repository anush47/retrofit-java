package com.retrofit.analysis.tools;

import org.springframework.stereotype.Component;

@Component
public class GetJavaVersionTool {
    public String execute() {
        return System.getProperty("java.version");
    }
}
