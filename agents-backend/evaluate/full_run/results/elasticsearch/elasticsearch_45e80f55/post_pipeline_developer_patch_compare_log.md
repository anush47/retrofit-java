# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']
- Developer Java files: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']
- Overlap Java files: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']

## File State Comparison
- Compared files: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']
- Mismatched files: ['libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java', 'libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -47,10 +47,10 @@
         for (String actionString : actionsList) {
             var action = ACTION_MAP.get(actionString);
             if (action == null) {
-                throw new IllegalArgumentException("unknown network action [" + actionString + "]");
+                throw new PolicyValidationException("unknown network action [" + actionString + "]");
             }
             if ((actionsInt & action) == action) {
-                throw new IllegalArgumentException(Strings.format("network action [%s] specified multiple times", actionString));
+                throw new PolicyValidationException(Strings.format("network action [%s] specified multiple times", actionString));
             }
             actionsInt |= action;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -47,10 +47,10 @@
-         for (String actionString : actionsList) {
-             var action = ACTION_MAP.get(actionString);
-             if (action == null) {
--                throw new IllegalArgumentException("unknown network action [" + actionString + "]");
-+                throw new PolicyValidationException("unknown network action [" + actionString + "]");
-             }
-             if ((actionsInt & action) == action) {
--                throw new IllegalArgumentException(Strings.format("network action [%s] specified multiple times", actionString));
-+                throw new PolicyValidationException(Strings.format("network action [%s] specified multiple times", actionString));
-             }
-             actionsInt |= action;
-         }
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java

- Developer hunks: 4
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -9,6 +9,7 @@
 
 package org.elasticsearch.entitlement.runtime.policy;
 
+import org.elasticsearch.xcontent.XContentLocation;
 import org.elasticsearch.xcontent.XContentParser;
 import org.elasticsearch.xcontent.XContentParserConfiguration;
 import org.elasticsearch.xcontent.yaml.YamlXContent;

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -9,6 +9,7 @@
- 
- package org.elasticsearch.entitlement.runtime.policy;
- 
-+import org.elasticsearch.xcontent.XContentLocation;
- import org.elasticsearch.xcontent.XContentParser;
- import org.elasticsearch.xcontent.XContentParserConfiguration;
- import org.elasticsearch.xcontent.yaml.YamlXContent;
+*No hunk*
```

#### Hunk 2

Developer
```diff
@@ -119,6 +120,7 @@
     }
 
     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
+        XContentLocation startLocation = policyParser.getTokenLocation();
         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
 
         if (entitlementClass == null) {

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,8 +1 @@-@@ -119,6 +120,7 @@
-     }
- 
-     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
-+        XContentLocation startLocation = policyParser.getTokenLocation();
-         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
- 
-         if (entitlementClass == null) {
+*No hunk*
```

#### Hunk 3

Developer
```diff
@@ -170,7 +172,10 @@
         try {
             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
-            throw new IllegalStateException("internal error");
+            if (e.getCause() instanceof PolicyValidationException piae) {
+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
+            }
+            throw new IllegalStateException("internal error", e);
         }
     }
 

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,12 +1 @@-@@ -170,7 +172,10 @@
-         try {
-             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
-         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
--            throw new IllegalStateException("internal error");
-+            if (e.getCause() instanceof PolicyValidationException piae) {
-+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
-+            }
-+            throw new IllegalStateException("internal error", e);
-         }
-     }
- 
+*No hunk*
```

#### Hunk 4

Developer
```diff
@@ -191,4 +196,13 @@
             message
         );
     }
+
+    protected PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
+    }
 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,14 +1 @@-@@ -191,4 +196,13 @@
-             message
-         );
-     }
-+
-+    protected PolicyParserException newPolicyParserException(
-+        XContentLocation location,
-+        String scopeName,
-+        String entitlementType,
-+        PolicyValidationException cause
-+    ) {
-+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
-+    }
- }
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -86,7 +86,36 @@
         }
     }
 
+    public static PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String policyName,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        assert (scopeName != null);
+        return new PolicyParserException(
+            "["
+                + location.lineNumber()
+                + ":"
+                + location.columnNumber()
+                + "] policy parsing error for ["
+                + policyName
+                + "] in scope ["
+                + scopeName
+                + "] for entitlement type ["
+                + entitlementType
+                + "]: "
+                + cause.getMessage(),
+            cause
+        );
+    }
+
     private PolicyParserException(String message) {
         super(message);
     }
+
+    private PolicyParserException(String message, PolicyValidationException cause) {
+        super(message, cause);
+    }
 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,37 +1 @@-@@ -86,7 +86,36 @@
-         }
-     }
- 
-+    public static PolicyParserException newPolicyParserException(
-+        XContentLocation location,
-+        String policyName,
-+        String scopeName,
-+        String entitlementType,
-+        PolicyValidationException cause
-+    ) {
-+        assert (scopeName != null);
-+        return new PolicyParserException(
-+            "["
-+                + location.lineNumber()
-+                + ":"
-+                + location.columnNumber()
-+                + "] policy parsing error for ["
-+                + policyName
-+                + "] in scope ["
-+                + scopeName
-+                + "] for entitlement type ["
-+                + entitlementType
-+                + "]: "
-+                + cause.getMessage(),
-+            cause
-+        );
-+    }
-+
-     private PolicyParserException(String message) {
-         super(message);
-     }
-+
-+    private PolicyParserException(String message, PolicyValidationException cause) {
-+        super(message, cause);
-+    }
- }
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -0,0 +1,27 @@
+/*
+ * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+ * or more contributor license agreements. Licensed under the "Elastic License
+ * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
+ * Public License v 1"; you may not use this file except in compliance with, at
+ * your election, the "Elastic License 2.0", the "GNU Affero General Public
+ * License v3.0 only", or the "Server Side Public License, v 1".
+ */
+
+package org.elasticsearch.entitlement.runtime.policy;
+
+/**
+ * This exception is used to track validation errors thrown during the construction
+ * of entitlements. By using this instead of other exception types the policy
+ * parser is able to wrap this exception with a line/character number for
+ * additional useful error information.
+ */
+class PolicyValidationException extends RuntimeException {
+
+    PolicyValidationException(String message) {
+        super(message);
+    }
+
+    PolicyValidationException(String message, Throwable cause) {
+        super(message, cause);
+    }
+}

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,28 +1 @@-@@ -0,0 +1,27 @@
-+/*
-+ * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
-+ * or more contributor license agreements. Licensed under the "Elastic License
-+ * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
-+ * Public License v 1"; you may not use this file except in compliance with, at
-+ * your election, the "Elastic License 2.0", the "GNU Affero General Public
-+ * License v3.0 only", or the "Server Side Public License, v 1".
-+ */
-+
-+package org.elasticsearch.entitlement.runtime.policy;
-+
-+/**
-+ * This exception is used to track validation errors thrown during the construction
-+ * of entitlements. By using this instead of other exception types the policy
-+ * parser is able to wrap this exception with a line/character number for
-+ * additional useful error information.
-+ */
-+class PolicyValidationException extends RuntimeException {
-+
-+    PolicyValidationException(String message) {
-+        super(message);
-+    }
-+
-+    PolicyValidationException(String message, Throwable cause) {
-+        super(message, cause);
-+    }
-+}
+*No hunk*
```


## Final Effective Hunk Comparison (agent + developer aux, code files)

### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -47,10 +47,10 @@
         for (String actionString : actionsList) {
             var action = ACTION_MAP.get(actionString);
             if (action == null) {
-                throw new IllegalArgumentException("unknown network action [" + actionString + "]");
+                throw new PolicyValidationException("unknown network action [" + actionString + "]");
             }
             if ((actionsInt & action) == action) {
-                throw new IllegalArgumentException(Strings.format("network action [%s] specified multiple times", actionString));
+                throw new PolicyValidationException(Strings.format("network action [%s] specified multiple times", actionString));
             }
             actionsInt |= action;
         }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,13 +1 @@-@@ -47,10 +47,10 @@
-         for (String actionString : actionsList) {
-             var action = ACTION_MAP.get(actionString);
-             if (action == null) {
--                throw new IllegalArgumentException("unknown network action [" + actionString + "]");
-+                throw new PolicyValidationException("unknown network action [" + actionString + "]");
-             }
-             if ((actionsInt & action) == action) {
--                throw new IllegalArgumentException(Strings.format("network action [%s] specified multiple times", actionString));
-+                throw new PolicyValidationException(Strings.format("network action [%s] specified multiple times", actionString));
-             }
-             actionsInt |= action;
-         }
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java

- Developer hunks: 4
- Generated hunks: 4

#### Hunk 1

Developer
```diff
@@ -9,6 +9,7 @@
 
 package org.elasticsearch.entitlement.runtime.policy;
 
+import org.elasticsearch.xcontent.XContentLocation;
 import org.elasticsearch.xcontent.XContentParser;
 import org.elasticsearch.xcontent.XContentParserConfiguration;
 import org.elasticsearch.xcontent.yaml.YamlXContent;

```

Generated
```diff
@@ -9,6 +9,7 @@
 
 package org.elasticsearch.entitlement.runtime.policy;
 
+import org.elasticsearch.xcontent.XContentLocation;
 import org.elasticsearch.xcontent.XContentParser;
 import org.elasticsearch.xcontent.XContentParserConfiguration;
 import org.elasticsearch.xcontent.yaml.YamlXContent;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -119,6 +120,7 @@
     }
 
     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
+        XContentLocation startLocation = policyParser.getTokenLocation();
         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
 
         if (entitlementClass == null) {

```

Generated
```diff
@@ -119,6 +120,7 @@
     }
 
     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
+        XContentLocation startLocation = policyParser.getTokenLocation();
         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
 
         if (entitlementClass == null) {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -170,7 +172,10 @@
         try {
             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
-            throw new IllegalStateException("internal error");
+            if (e.getCause() instanceof PolicyValidationException piae) {
+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
+            }
+            throw new IllegalStateException("internal error", e);
         }
     }
 

```

Generated
```diff
@@ -170,7 +172,10 @@
         try {
             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
-            throw new IllegalStateException("internal error");
+            if (e.getCause() instanceof PolicyValidationException piae) {
+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
+            }
+            throw new IllegalStateException("internal error", e);
         }
     }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -191,4 +196,13 @@
             message
         );
     }
+
+    protected PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
+    }
 }

```

Generated
```diff
@@ -191,4 +196,13 @@
             message
         );
     }
+
+    protected PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
+    }
 }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -86,7 +86,36 @@
         }
     }
 
+    public static PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String policyName,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        assert (scopeName != null);
+        return new PolicyParserException(
+            "["
+                + location.lineNumber()
+                + ":"
+                + location.columnNumber()
+                + "] policy parsing error for ["
+                + policyName
+                + "] in scope ["
+                + scopeName
+                + "] for entitlement type ["
+                + entitlementType
+                + "]: "
+                + cause.getMessage(),
+            cause
+        );
+    }
+
     private PolicyParserException(String message) {
         super(message);
     }
+
+    private PolicyParserException(String message, PolicyValidationException cause) {
+        super(message, cause);
+    }
 }

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,37 +1 @@-@@ -86,7 +86,36 @@
-         }
-     }
- 
-+    public static PolicyParserException newPolicyParserException(
-+        XContentLocation location,
-+        String policyName,
-+        String scopeName,
-+        String entitlementType,
-+        PolicyValidationException cause
-+    ) {
-+        assert (scopeName != null);
-+        return new PolicyParserException(
-+            "["
-+                + location.lineNumber()
-+                + ":"
-+                + location.columnNumber()
-+                + "] policy parsing error for ["
-+                + policyName
-+                + "] in scope ["
-+                + scopeName
-+                + "] for entitlement type ["
-+                + entitlementType
-+                + "]: "
-+                + cause.getMessage(),
-+            cause
-+        );
-+    }
-+
-     private PolicyParserException(String message) {
-         super(message);
-     }
-+
-+    private PolicyParserException(String message, PolicyValidationException cause) {
-+        super(message, cause);
-+    }
- }
+*No hunk*
```


### libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java

- Developer hunks: 1
- Generated hunks: 0

#### Hunk 1

Developer
```diff
@@ -0,0 +1,27 @@
+/*
+ * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+ * or more contributor license agreements. Licensed under the "Elastic License
+ * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
+ * Public License v 1"; you may not use this file except in compliance with, at
+ * your election, the "Elastic License 2.0", the "GNU Affero General Public
+ * License v3.0 only", or the "Server Side Public License, v 1".
+ */
+
+package org.elasticsearch.entitlement.runtime.policy;
+
+/**
+ * This exception is used to track validation errors thrown during the construction
+ * of entitlements. By using this instead of other exception types the policy
+ * parser is able to wrap this exception with a line/character number for
+ * additional useful error information.
+ */
+class PolicyValidationException extends RuntimeException {
+
+    PolicyValidationException(String message) {
+        super(message);
+    }
+
+    PolicyValidationException(String message, Throwable cause) {
+        super(message, cause);
+    }
+}

```

Generated
```diff
*No hunk*
```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,28 +1 @@-@@ -0,0 +1,27 @@
-+/*
-+ * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
-+ * or more contributor license agreements. Licensed under the "Elastic License
-+ * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
-+ * Public License v 1"; you may not use this file except in compliance with, at
-+ * your election, the "Elastic License 2.0", the "GNU Affero General Public
-+ * License v3.0 only", or the "Server Side Public License, v 1".
-+ */
-+
-+package org.elasticsearch.entitlement.runtime.policy;
-+
-+/**
-+ * This exception is used to track validation errors thrown during the construction
-+ * of entitlements. By using this instead of other exception types the policy
-+ * parser is able to wrap this exception with a line/character number for
-+ * additional useful error information.
-+ */
-+class PolicyValidationException extends RuntimeException {
-+
-+    PolicyValidationException(String message) {
-+        super(message);
-+    }
-+
-+    PolicyValidationException(String message, Throwable cause) {
-+        super(message, cause);
-+    }
-+}
+*No hunk*
```



## Full Generated Patch (Agent-Only, code-only)
```diff

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
@@ -9,6 +9,7 @@
 
 package org.elasticsearch.entitlement.runtime.policy;
 
+import org.elasticsearch.xcontent.XContentLocation;
 import org.elasticsearch.xcontent.XContentParser;
 import org.elasticsearch.xcontent.XContentParserConfiguration;
 import org.elasticsearch.xcontent.yaml.YamlXContent;
@@ -119,6 +120,7 @@
     }
 
     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
+        XContentLocation startLocation = policyParser.getTokenLocation();
         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
 
         if (entitlementClass == null) {
@@ -170,7 +172,10 @@
         try {
             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
-            throw new IllegalStateException("internal error");
+            if (e.getCause() instanceof PolicyValidationException piae) {
+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
+            }
+            throw new IllegalStateException("internal error", e);
         }
     }
 
@@ -191,4 +196,13 @@
             message
         );
     }
+
+    protected PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
+    }
 }

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java
index 9b4035cee98..ea78c8cafc9 100644
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/NetworkEntitlement.java
@@ -47,10 +47,10 @@ public class NetworkEntitlement implements Entitlement {
         for (String actionString : actionsList) {
             var action = ACTION_MAP.get(actionString);
             if (action == null) {
-                throw new IllegalArgumentException("unknown network action [" + actionString + "]");
+                throw new PolicyValidationException("unknown network action [" + actionString + "]");
             }
             if ((actionsInt & action) == action) {
-                throw new IllegalArgumentException(Strings.format("network action [%s] specified multiple times", actionString));
+                throw new PolicyValidationException(Strings.format("network action [%s] specified multiple times", actionString));
             }
             actionsInt |= action;
         }
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
index ac4d4afdd97..42c0da8444b 100644
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java
@@ -9,6 +9,7 @@
 
 package org.elasticsearch.entitlement.runtime.policy;
 
+import org.elasticsearch.xcontent.XContentLocation;
 import org.elasticsearch.xcontent.XContentParser;
 import org.elasticsearch.xcontent.XContentParserConfiguration;
 import org.elasticsearch.xcontent.yaml.YamlXContent;
@@ -119,6 +120,7 @@ public class PolicyParser {
     }
 
     protected Entitlement parseEntitlement(String scopeName, String entitlementType) throws IOException {
+        XContentLocation startLocation = policyParser.getTokenLocation();
         Class<?> entitlementClass = EXTERNAL_ENTITLEMENTS.get(entitlementType);
 
         if (entitlementClass == null) {
@@ -170,7 +172,10 @@ public class PolicyParser {
         try {
             return (Entitlement) entitlementConstructor.newInstance(parameterValues);
         } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
-            throw new IllegalStateException("internal error");
+            if (e.getCause() instanceof PolicyValidationException piae) {
+                throw newPolicyParserException(startLocation, scopeName, entitlementType, piae);
+            }
+            throw new IllegalStateException("internal error", e);
         }
     }
 
@@ -191,4 +196,13 @@ public class PolicyParser {
             message
         );
     }
+
+    protected PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        return PolicyParserException.newPolicyParserException(location, policyName, scopeName, entitlementType, cause);
+    }
 }
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java
index 5dfa12f11d0..e7cc8bed2ca 100644
--- a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java
@@ -86,7 +86,36 @@ public class PolicyParserException extends RuntimeException {
         }
     }
 
+    public static PolicyParserException newPolicyParserException(
+        XContentLocation location,
+        String policyName,
+        String scopeName,
+        String entitlementType,
+        PolicyValidationException cause
+    ) {
+        assert (scopeName != null);
+        return new PolicyParserException(
+            "["
+                + location.lineNumber()
+                + ":"
+                + location.columnNumber()
+                + "] policy parsing error for ["
+                + policyName
+                + "] in scope ["
+                + scopeName
+                + "] for entitlement type ["
+                + entitlementType
+                + "]: "
+                + cause.getMessage(),
+            cause
+        );
+    }
+
     private PolicyParserException(String message) {
         super(message);
     }
+
+    private PolicyParserException(String message, PolicyValidationException cause) {
+        super(message, cause);
+    }
 }
diff --git a/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java
new file mode 100644
index 00000000000..a2bc49d99b4
--- /dev/null
+++ b/libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyValidationException.java
@@ -0,0 +1,27 @@
+/*
+ * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+ * or more contributor license agreements. Licensed under the "Elastic License
+ * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
+ * Public License v 1"; you may not use this file except in compliance with, at
+ * your election, the "Elastic License 2.0", the "GNU Affero General Public
+ * License v3.0 only", or the "Server Side Public License, v 1".
+ */
+
+package org.elasticsearch.entitlement.runtime.policy;
+
+/**
+ * This exception is used to track validation errors thrown during the construction
+ * of entitlements. By using this instead of other exception types the policy
+ * parser is able to wrap this exception with a line/character number for
+ * additional useful error information.
+ */
+class PolicyValidationException extends RuntimeException {
+
+    PolicyValidationException(String message) {
+        super(message);
+    }
+
+    PolicyValidationException(String message, Throwable cause) {
+        super(message, cause);
+    }
+}
diff --git a/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserTests.java b/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserTests.java
index 1e0c31d2280..2951ac19065 100644
--- a/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserTests.java
+++ b/libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserTests.java
@@ -68,6 +68,24 @@ public class PolicyParserTests extends ESTestCase {
         assertEquals(expected, parsedPolicy);
     }
 
+    public void testParseNetworkIllegalAction() throws IOException {
+        var ex = expectThrows(PolicyParserException.class, () -> new PolicyParser(new ByteArrayInputStream("""
+            entitlement-module-name:
+              - network:
+                  actions:
+                    - listen
+                    - doesnotexist
+                    - connect
+            """.getBytes(StandardCharsets.UTF_8)), "test-policy.yaml", false).parsePolicy());
+        assertThat(
+            ex.getMessage(),
+            equalTo(
+                "[2:5] policy parsing error for [test-policy.yaml] in scope [entitlement-module-name] for entitlement type [network]: "
+                    + "unknown network action [doesnotexist]"
+            )
+        );
+    }
+
     public void testParseCreateClassloader() throws IOException {
         Policy parsedPolicy = new PolicyParser(new ByteArrayInputStream("""
             entitlement-module-name:

```
