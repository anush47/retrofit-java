# Post-Pipeline Developer Patch Comparison

**Exact Developer Patch (code-only)**: False

**Comparison Method**: file_state

## Commit Pair Consistency
- Pair mismatch: False
- Reason: scope_overlap_ok
- Mainline Java files: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java', 'server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java', 'server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java']
- Developer Java files: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java', 'server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java', 'server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java']
- Overlap Java files: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java', 'server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java', 'server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java']
- Overlap ratio (mainline): 1.0
- Compare files scope used: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java', 'server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java', 'server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java']

## File State Comparison
- Compared files: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java', 'server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java', 'server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java', 'server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java', 'server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java']
- Mismatched files: ['server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java']
- Error: None

## Comparison Scope
- Agent-only patch: code hunks produced by Agent 3
- Final effective patch: agent code hunks + developer auxiliary hunks (still code-only for this report)

## Agent-Only Hunk Comparison (code files)

### server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java

- Developer hunks: 1
- Generated hunks: 1

#### Hunk 1

Developer
```diff
@@ -0,0 +1,355 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import java.net.SocketAddress;
+import java.util.ArrayDeque;
+
+import org.jetbrains.annotations.Nullable;
+
+import io.netty.buffer.ByteBufAllocator;
+import io.netty.channel.Channel;
+import io.netty.channel.ChannelConfig;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelId;
+import io.netty.channel.ChannelMetadata;
+import io.netty.channel.ChannelPipeline;
+import io.netty.channel.ChannelProgressivePromise;
+import io.netty.channel.ChannelPromise;
+import io.netty.channel.EventLoop;
+import io.netty.util.Attribute;
+import io.netty.util.AttributeKey;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * Channel implementation that allows to delay writes with `blockWritesUntil`
+ **/
+public class DelayableWriteChannel implements Channel {
+
+    private final Channel delegate;
+    private DelayedWrites delay = null;
+
+    public DelayableWriteChannel(Channel channel) {
+        this.delegate = channel;
+        channel.closeFuture().addListener(_ -> discardDelayedWrites());
+    }
+
+    @Override
+    public <T> Attribute<T> attr(AttributeKey<T> key) {
+        return delegate.attr(key);
+    }
+
+    @Override
+    public <T> boolean hasAttr(AttributeKey<T> key) {
+        return delegate.hasAttr(key);
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress) {
+        return delegate.bind(localAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress) {
+        return delegate.connect(remoteAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress) {
+        return delegate.connect(remoteAddress, localAddress);
+    }
+
+    @Override
+    public ChannelFuture disconnect() {
+        return delegate.disconnect();
+    }
+
+    @Override
+    public ChannelFuture close() {
+        return delegate.close();
+    }
+
+    @Override
+    public ChannelFuture deregister() {
+        return delegate.deregister();
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.bind(localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture disconnect(ChannelPromise promise) {
+        return delegate.disconnect(promise);
+    }
+
+    @Override
+    public ChannelFuture close(ChannelPromise promise) {
+        return delegate.close(promise);
+    }
+
+    @Override
+    public ChannelFuture deregister(ChannelPromise promise) {
+        return delegate.deregister(promise);
+    }
+
+    @Override
+    public ChannelFuture write(Object msg) {
+        return this.write(msg, newPromise());
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg) {
+        return this.writeAndFlush(msg, newPromise());
+    }
+
+    @Override
+    public ChannelPromise newPromise() {
+        return delegate.newPromise();
+    }
+
+    @Override
+    public ChannelProgressivePromise newProgressivePromise() {
+        return delegate.newProgressivePromise();
+    }
+
+    @Override
+    public ChannelFuture newSucceededFuture() {
+        return delegate.newSucceededFuture();
+    }
+
+    @Override
+    public ChannelFuture newFailedFuture(Throwable cause) {
+        return delegate.newFailedFuture(cause);
+    }
+
+    @Override
+    public ChannelPromise voidPromise() {
+        return delegate.voidPromise();
+    }
+
+    @Override
+    public int compareTo(Channel o) {
+        return delegate.compareTo(o);
+    }
+
+    @Override
+    public ChannelId id() {
+        return delegate.id();
+    }
+
+    @Override
+    public EventLoop eventLoop() {
+        return delegate.eventLoop();
+    }
+
+    @Override
+    public Channel parent() {
+        return delegate.parent();
+    }
+
+    @Override
+    public ChannelConfig config() {
+        return delegate.config();
+    }
+
+    @Override
+    public boolean isOpen() {
+        return delegate.isOpen();
+    }
+
+    @Override
+    public boolean isRegistered() {
+        return delegate.isRegistered();
+    }
+
+    @Override
+    public boolean isActive() {
+        return delegate.isActive();
+    }
+
+    @Override
+    public ChannelMetadata metadata() {
+        return delegate.metadata();
+    }
+
+    @Override
+    public SocketAddress localAddress() {
+        return delegate.localAddress();
+    }
+
+    @Override
+    public SocketAddress remoteAddress() {
+        return delegate.remoteAddress();
+    }
+
+    @Override
+    public ChannelFuture closeFuture() {
+        return delegate.closeFuture();
+    }
+
+    @Override
+    public boolean isWritable() {
+        return delegate.isWritable();
+    }
+
+    @Override
+    public long bytesBeforeUnwritable() {
+        return delegate.bytesBeforeUnwritable();
+    }
+
+    @Override
+    public long bytesBeforeWritable() {
+        return delegate.bytesBeforeWritable();
+    }
+
+    @Override
+    public Unsafe unsafe() {
+        return delegate.unsafe();
+    }
+
+    @Override
+    public ChannelPipeline pipeline() {
+        return delegate.pipeline();
+    }
+
+    @Override
+    public ByteBufAllocator alloc() {
+        return delegate.alloc();
+    }
+
+    @Override
+    public Channel read() {
+        return delegate.read();
+    }
+
+    @Override
+    public Channel flush() {
+        return delegate.flush();
+    }
+
+    public Channel bypassDelay() {
+        return delegate;
+    }
+
+
+    @Override
+    public ChannelFuture write(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.write(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.write(msg, promise);
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.writeAndFlush(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.writeAndFlush(msg, promise);
+    }
+
+    public synchronized void discardDelayedWrites() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.discard();
+                parent = parent.parent;
+            }
+            delay.discard();
+            delay = null;
+        }
+    }
+
+    public synchronized void writePendingMessages(DelayedWrites delayedWrites) {
+        if (delay == delayedWrites) {
+            delay = null;
+        }
+        delayedWrites.writeDelayed();
+    }
+
+    public synchronized void writePendingMessages() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.writeDelayed();
+                parent = parent.parent;
+            }
+            delay.writeDelayed();
+            delay = null;
+        }
+    }
+
+    public DelayedWrites delayWrites() {
+        DelayedWrites delayedWrites = new DelayedWrites(delay);
+        delay = delayedWrites;
+        return delayedWrites;
+    }
+
+    record DelayedMsg(Object msg, Runnable runnable) {
+    }
+
+    static class DelayedWrites {
+
+        private final ArrayDeque<DelayedMsg> delayed = new ArrayDeque<>();
+        private final DelayedWrites parent;
+
+        public DelayedWrites(@Nullable DelayedWrites parent) {
+            this.parent = parent;
+        }
+
+        public void discard() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                ReferenceCountUtil.safeRelease(delayedMsg.msg);
+            }
+        }
+
+        public void add(Object msg, Runnable runnable) {
+            delayed.add(new DelayedMsg(msg, runnable));
+        }
+
+        private void writeDelayed() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                delayedMsg.runnable.run();
+            }
+        }
+    }
+}

```

Generated
```diff
@@ -0,0 +1,352 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import java.net.SocketAddress;
+import java.util.ArrayDeque;
+
+import org.jetbrains.annotations.Nullable;
+
+import io.netty.buffer.ByteBufAllocator;
+import io.netty.channel.Channel;
+import io.netty.channel.ChannelConfig;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelId;
+import io.netty.channel.ChannelMetadata;
+import io.netty.channel.ChannelPipeline;
+import io.netty.channel.ChannelProgressivePromise;
+import io.netty.channel.ChannelPromise;
+import io.netty.channel.EventLoop;
+import io.netty.util.Attribute;
+import io.netty.util.AttributeKey;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * Channel implementation that allows to delay writes with `blockWritesUntil`
+ **/
+public class DelayableWriteChannel implements Channel {
+
+    private final Channel delegate;
+    private DelayedWrites delay = null;
+
+    public DelayableWriteChannel(Channel channel) {
+        this.delegate = channel;
+        channel.closeFuture().addListener(_ -> discardDelayedWrites());
+    }
+
+    @Override
+    public <T> Attribute<T> attr(AttributeKey<T> key) {
+        return delegate.attr(key);
+    }
+
+    @Override
+    public <T> boolean hasAttr(AttributeKey<T> key) {
+        return delegate.hasAttr(key);
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress) {
+        return delegate.bind(localAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress) {
+        return delegate.connect(remoteAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress) {
+        return delegate.connect(remoteAddress, localAddress);
+    }
+
+    @Override
+    public ChannelFuture disconnect() {
+        return delegate.disconnect();
+    }
+
+    @Override
+    public ChannelFuture close() {
+        return delegate.close();
+    }
+
+    @Override
+    public ChannelFuture deregister() {
+        return delegate.deregister();
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.bind(localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture disconnect(ChannelPromise promise) {
+        return delegate.disconnect(promise);
+    }
+
+    @Override
+    public ChannelFuture close(ChannelPromise promise) {
+        return delegate.close(promise);
+    }
+
+    @Override
+    public ChannelFuture deregister(ChannelPromise promise) {
+        return delegate.deregister(promise);
+    }
+
+    @Override
+    public ChannelFuture write(Object msg) {
+        return this.write(msg, newPromise());
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg) {
+        return this.writeAndFlush(msg, newPromise());
+    }
+
+    @Override
+    public ChannelPromise newPromise() {
+        return delegate.newPromise();
+    }
+
+    @Override
+    public ChannelProgressivePromise newProgressivePromise() {
+        return delegate.newProgressivePromise();
+    }
+
+    @Override
+    public ChannelFuture newSucceededFuture() {
+        return delegate.newSucceededFuture();
+    }
+
+    @Override
+    public ChannelFuture newFailedFuture(Throwable cause) {
+        return delegate.newFailedFuture(cause);
+    }
+
+    @Override
+    public ChannelPromise voidPromise() {
+        return delegate.voidPromise();
+    }
+
+    @Override
+    public int compareTo(Channel o) {
+        return delegate.compareTo(o);
+    }
+
+    @Override
+    public ChannelId id() {
+        return delegate.id();
+    }
+
+    @Override
+    public EventLoop eventLoop() {
+        return delegate.eventLoop();
+    }
+
+    @Override
+    public Channel parent() {
+        return delegate.parent();
+    }
+
+    @Override
+    public ChannelConfig config() {
+        return delegate.config();
+    }
+
+    @Override
+    public boolean isOpen() {
+        return delegate.isOpen();
+    }
+
+    @Override
+    public boolean isRegistered() {
+        return delegate.isRegistered();
+    }
+
+    @Override
+    public boolean isActive() {
+        return delegate.isActive();
+    }
+
+    @Override
+    public ChannelMetadata metadata() {
+        return delegate.metadata();
+    }
+
+    @Override
+    public SocketAddress localAddress() {
+        return delegate.localAddress();
+    }
+
+    @Override
+    public SocketAddress remoteAddress() {
+        return delegate.remoteAddress();
+    }
+
+    @Override
+    public ChannelFuture closeFuture() {
+        return delegate.closeFuture();
+    }
+
+    @Override
+    public boolean isWritable() {
+        return delegate.isWritable();
+    }
+
+    @Override
+    public long bytesBeforeUnwritable() {
+        return delegate.bytesBeforeUnwritable();
+    }
+
+    @Override
+    public long bytesBeforeWritable() {
+        return delegate.bytesBeforeWritable();
+    }
+
+    @Override
+    public Unsafe unsafe() {
+        return delegate.unsafe();
+    }
+
+    @Override
+    public ChannelPipeline pipeline() {
+        return delegate.pipeline();
+    }
+
+    @Override
+    public ByteBufAllocator alloc() {
+        return delegate.alloc();
+    }
+
+    @Override
+    public Channel read() {
+        return delegate.read();
+    }
+
+    @Override
+    public Channel flush() {
+        return delegate.flush();
+    }
+
+    public Channel bypassDelay() {
+        return delegate;
+    }
+
+
+    @Override
+    public ChannelFuture write(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.write(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.write(msg, promise);
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.writeAndFlush(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.writeAndFlush(msg, promise);
+    }
+
+    public synchronized void discardDelayedWrites() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.discard();
+                parent = parent.parent;
+            }
+            delay.discard();
+            delay = null;
+        }
+    }
+
+    public synchronized void writePendingMessages(DelayedWrites delayedWrites) {
+        if (delay == delayedWrites) {
+            delay = null;
+        }
+        delayedWrites.writeDelayed();
+    }
+
+    public synchronized void writePendingMessages() {
+        if (delay == null) {
+            return;
+        }
+        DelayedWrites delayedWrites = delay;
+        delay = null;
+        delayedWrites.writeDelayed();
+    }
+
+    public DelayedWrites delayWrites() {
+        DelayedWrites delayedWrites = new DelayedWrites(delay);
+        delay = delayedWrites;
+        return delayedWrites;
+    }
+
+    record DelayedMsg(Object msg, Runnable runnable) {
+    }
+
+    static class DelayedWrites {
+
+        private final ArrayDeque<DelayedMsg> delayed = new ArrayDeque<>();
+        private final DelayedWrites parent;
+
+        public DelayedWrites(@Nullable DelayedWrites parent) {
+            this.parent = parent;
+        }
+
+        public void discard() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                ReferenceCountUtil.safeRelease(delayedMsg.msg);
+            }
+        }
+
+        public void add(Object msg, Runnable runnable) {
+            delayed.add(new DelayedMsg(msg, runnable));
+        }
+
+        private void writeDelayed() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                delayedMsg.runnable.run();
+            }
+        }
+    }
+}

```

Developer -> Generated (Unified Diff)
```diff
--- developer+++ generated@@ -1,4 +1,4 @@-@@ -0,0 +1,355 @@
+@@ -0,0 +1,352 @@
 +/*
 + * Licensed to Crate.io GmbH ("Crate") under one or more contributor
 + * license agreements.  See the NOTICE file distributed with this work for
@@ -306,15 +306,12 @@ +    }
 +
 +    public synchronized void writePendingMessages() {
-+        if (delay != null) {
-+            var parent = delay.parent;
-+            while (parent != null) {
-+                parent.writeDelayed();
-+                parent = parent.parent;
-+            }
-+            delay.writeDelayed();
-+            delay = null;
-+        }
++        if (delay == null) {
++            return;
++        }
++        DelayedWrites delayedWrites = delay;
++        delay = null;
++        delayedWrites.writeDelayed();
 +    }
 +
 +    public DelayedWrites delayWrites() {

```


### server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java

- Developer hunks: 3
- Generated hunks: 3

#### Hunk 1

Developer
```diff
@@ -70,7 +70,6 @@
 import io.netty.bootstrap.ServerBootstrap;
 import io.netty.channel.Channel;
 import io.netty.channel.ChannelInitializer;
-import io.netty.channel.ChannelOption;
 import io.netty.channel.ChannelPipeline;
 import io.netty.handler.ssl.SslContext;
 

```

Generated
```diff
@@ -70,7 +70,6 @@
 import io.netty.bootstrap.ServerBootstrap;
 import io.netty.channel.Channel;
 import io.netty.channel.ChannelInitializer;
-import io.netty.channel.ChannelOption;
 import io.netty.channel.ChannelPipeline;
 import io.netty.handler.ssl.SslContext;
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -168,7 +167,6 @@
         }
         var eventLoopGroup = nettyBootstrap.getSharedEventLoopGroup();
         bootstrap = NettyBootstrap.newServerBootstrap(settings, eventLoopGroup);
-        bootstrap.childOption(ChannelOption.AUTO_READ, false);
         inboundStatsHandler = new Netty4InboundStatsHandler(statsTracker, LOGGER);
         outboundStatsHandler = new Netty4OutboundStatsHandler(statsTracker, LOGGER);
 

```

Generated
```diff
@@ -168,7 +167,6 @@
         }
         var eventLoopGroup = nettyBootstrap.getSharedEventLoopGroup();
         bootstrap = NettyBootstrap.newServerBootstrap(settings, eventLoopGroup);
-        bootstrap.childOption(ChannelOption.AUTO_READ, false);
         inboundStatsHandler = new Netty4InboundStatsHandler(statsTracker, LOGGER);
         outboundStatsHandler = new Netty4OutboundStatsHandler(statsTracker, LOGGER);
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -189,8 +187,7 @@
                     chPipeline -> {
                         var nettyTcpChannel = new CloseableChannel(ch, true);
                         ch.attr(Netty4Transport.CHANNEL_KEY).set(nettyTcpChannel);
-                        var handler = new Netty4MessageChannelHandler(pageCacheRecycler, transport, false);
-                        chPipeline.addLast("dispatcher", handler);
+                        chPipeline.addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, transport));
                     },
                     authentication,
                     sslContextProvider

```

Generated
```diff
@@ -189,8 +187,7 @@
                     chPipeline -> {
                         var nettyTcpChannel = new CloseableChannel(ch, true);
                         ch.attr(Netty4Transport.CHANNEL_KEY).set(nettyTcpChannel);
-                        var handler = new Netty4MessageChannelHandler(pageCacheRecycler, transport, false);
-                        chPipeline.addLast("dispatcher", handler);
+                        chPipeline.addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, transport));
                     },
                     authentication,
                     sslContextProvider

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java

- Developer hunks: 20
- Generated hunks: 20

#### Hunk 1

Developer
```diff
@@ -61,6 +61,7 @@
 import io.crate.metadata.settings.CoordinatorSessionSettings;
 import io.crate.metadata.settings.session.SessionSetting;
 import io.crate.metadata.settings.session.SessionSettingRegistry;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.role.Role;

```

Generated
```diff
@@ -61,6 +61,7 @@
 import io.crate.metadata.settings.CoordinatorSessionSettings;
 import io.crate.metadata.settings.session.SessionSetting;
 import io.crate.metadata.settings.session.SessionSettingRegistry;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.role.Role;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -205,7 +206,7 @@
     private final Authentication authService;
     private final Consumer<ChannelPipeline> addTransportHandler;
 
-    private Channel channel;
+    private DelayableWriteChannel channel;
     Session session;
     private boolean ignoreTillSync = false;
     private AuthenticationContext authContext;

```

Generated
```diff
@@ -205,7 +206,7 @@
     private final Authentication authService;
     private final Consumer<ChannelPipeline> addTransportHandler;
 
-    private Channel channel;
+    private DelayableWriteChannel channel;
     Session session;
     private boolean ignoreTillSync = false;
     private AuthenticationContext authContext;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -265,10 +266,8 @@
     private static class ReadyForQueryCallback implements BiConsumer<Object, Throwable> {
         private final Channel channel;
         private final TransactionState transactionState;
-        private final Runnable read;
 
-        private ReadyForQueryCallback(Runnable read, Channel channel, TransactionState transactionState) {
-            this.read = read;
+        private ReadyForQueryCallback(Channel channel, TransactionState transactionState) {
             this.channel = channel;
             this.transactionState = transactionState;
         }

```

Generated
```diff
@@ -265,10 +266,8 @@
     private static class ReadyForQueryCallback implements BiConsumer<Object, Throwable> {
         private final Channel channel;
         private final TransactionState transactionState;
-        private final Runnable read;
 
-        private ReadyForQueryCallback(Runnable read, Channel channel, TransactionState transactionState) {
-            this.read = read;
+        private ReadyForQueryCallback(Channel channel, TransactionState transactionState) {
             this.channel = channel;
             this.transactionState = transactionState;
         }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -276,7 +275,6 @@
         @Override
         public void accept(Object result, Throwable t) {
             sendReadyForQuery(channel, transactionState);
-            read.run();
         }
     }
 

```

Generated
```diff
@@ -276,7 +275,6 @@
         @Override
         public void accept(Object result, Throwable t) {
             sendReadyForQuery(channel, transactionState);
-            read.run();
         }
     }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 5

Developer
```diff
@@ -284,7 +282,7 @@
 
         @Override
         public void channelRegistered(ChannelHandlerContext ctx) throws Exception {
-            channel = ctx.channel();
+            channel = new DelayableWriteChannel(ctx.channel());
         }
 
         @Override

```

Generated
```diff
@@ -284,7 +282,7 @@
 
         @Override
         public void channelRegistered(ChannelHandlerContext ctx) throws Exception {
-            channel = ctx.channel();
+            channel = new DelayableWriteChannel(ctx.channel());
         }
 
         @Override

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 6

Developer
```diff
@@ -292,17 +290,11 @@
             return true;
         }
 
-        @Override
-        public void channelActive(ChannelHandlerContext ctx) throws Exception {
-            super.channelActive(ctx);
-            ctx.read();
-        }
-
         @Override
         public void channelRead0(ChannelHandlerContext ctx, ByteBuf buffer) throws Exception {
             assert channel != null : "Channel must be initialized";
             try {
-                dispatchState(ctx, buffer, channel);
+                dispatchState(buffer, channel);
             } catch (Throwable t) {
                 ignoreTillSync = true;
                 try {

```

Generated
```diff
@@ -292,17 +290,11 @@
             return true;
         }
 
-        @Override
-        public void channelActive(ChannelHandlerContext ctx) throws Exception {
-            super.channelActive(ctx);
-            ctx.read();
-        }
-
         @Override
         public void channelRead0(ChannelHandlerContext ctx, ByteBuf buffer) throws Exception {
             assert channel != null : "Channel must be initialized";
             try {
-                dispatchState(ctx, buffer, channel);
+                dispatchState(buffer, channel);
             } catch (Throwable t) {
                 ignoreTillSync = true;
                 try {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 7

Developer
```diff
@@ -313,21 +305,18 @@
                 } catch (Throwable ti) {
                     LOGGER.error("Error trying to send error to client: {}", t, ti);
                 }
-                ctx.read();
             }
         }
 
-        private void dispatchState(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchState(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.state()) {
                 case STARTUP_PARAMETERS:
                     handleStartupBody(buffer, channel);
                     decoder.startupDone();
-                    ctx.read();
                     return;
 
                 case CANCEL:
                     handleCancelRequestBody(buffer, channel);
-                    ctx.read();
                     return;
 
                 case MSG:

```

Generated
```diff
@@ -313,21 +305,18 @@
                 } catch (Throwable ti) {
                     LOGGER.error("Error trying to send error to client: {}", t, ti);
                 }
-                ctx.read();
             }
         }
 
-        private void dispatchState(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchState(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.state()) {
                 case STARTUP_PARAMETERS:
                     handleStartupBody(buffer, channel);
                     decoder.startupDone();
-                    ctx.read();
                     return;
 
                 case CANCEL:
                     handleCancelRequestBody(buffer, channel);
-                    ctx.read();
                     return;
 
                 case MSG:

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 8

Developer
```diff
@@ -335,55 +324,47 @@
 
                     if (ignoreTillSync && decoder.msgType() != 'S') {
                         buffer.skipBytes(decoder.payloadLength());
-                        ctx.read();
                         return;
                     }
-                    dispatchMessage(ctx, buffer, channel);
+                    dispatchMessage(buffer, channel);
                     return;
                 default:
                     throw new IllegalStateException("Illegal state: " + decoder.state());
             }
         }
 
-        private void dispatchMessage(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchMessage(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.msgType()) {
                 case 'Q': // Query (simple)
-                    handleSimpleQuery(ctx::read, buffer, channel);
+                    handleSimpleQuery(buffer, channel);
                     return;
                 case 'P':
                     handleParseMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'p':
                     handlePassword(buffer, channel);
-                    ctx.read();
                     return;
                 case 'B':
                     handleBindMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'D':
                     handleDescribeMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'E':
-                    handleExecute(ctx, buffer, channel);
+                    handleExecute(buffer, channel);
                     return;
                 case 'H':
                     handleFlush(channel);
-                    ctx.read();
                     return;
                 case 'S':
-                    handleSync(ctx, channel);
+                    handleSync(channel);
                     return;
                 case 'C':
                     handleClose(buffer, channel);
-                    ctx.read();
                     return;
                 case 'X': // Terminate (called when jdbc connection is closed)
                     closeSession();
                     channel.close();
-                    ctx.read();
                     return;
                 default:
                     Messages.sendErrorResponse(

```

Generated
```diff
@@ -335,55 +324,47 @@
 
                     if (ignoreTillSync && decoder.msgType() != 'S') {
                         buffer.skipBytes(decoder.payloadLength());
-                        ctx.read();
                         return;
                     }
-                    dispatchMessage(ctx, buffer, channel);
+                    dispatchMessage(buffer, channel);
                     return;
                 default:
                     throw new IllegalStateException("Illegal state: " + decoder.state());
             }
         }
 
-        private void dispatchMessage(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchMessage(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.msgType()) {
                 case 'Q': // Query (simple)
-                    handleSimpleQuery(ctx::read, buffer, channel);
+                    handleSimpleQuery(buffer, channel);
                     return;
                 case 'P':
                     handleParseMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'p':
                     handlePassword(buffer, channel);
-                    ctx.read();
                     return;
                 case 'B':
                     handleBindMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'D':
                     handleDescribeMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'E':
-                    handleExecute(ctx, buffer, channel);
+                    handleExecute(buffer, channel);
                     return;
                 case 'H':
                     handleFlush(channel);
-                    ctx.read();
                     return;
                 case 'S':
-                    handleSync(ctx, channel);
+                    handleSync(channel);
                     return;
                 case 'C':
                     handleClose(buffer, channel);
-                    ctx.read();
                     return;
                 case 'X': // Terminate (called when jdbc connection is closed)
                     closeSession();
                     channel.close();
-                    ctx.read();
                     return;
                 default:
                     Messages.sendErrorResponse(

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 9

Developer
```diff
@@ -392,7 +373,6 @@
                             ? AccessControl.DISABLED
                             : getAccessControl.apply(session.sessionSettings()),
                         new UnsupportedOperationException("Unsupported messageType: " + decoder.msgType()));
-                    ctx.read();
             }
         }
 

```

Generated
```diff
@@ -392,7 +373,6 @@
                             ? AccessControl.DISABLED
                             : getAccessControl.apply(session.sessionSettings()),
                         new UnsupportedOperationException("Unsupported messageType: " + decoder.msgType()));
-                    ctx.read();
             }
         }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 10

Developer
```diff
@@ -479,9 +459,9 @@
                 applyOptions(options);
             }
             Messages.sendAuthenticationOK(channel)
-                .addListener(_ -> sendParams(channel, session.sessionSettings()))
-                .addListener(_ -> Messages.sendKeyData(channel, session.id(), session.secret()))
-                .addListener(_ -> {
+                .addListener(f -> sendParams(channel, session.sessionSettings()))
+                .addListener(f -> Messages.sendKeyData(channel, session.id(), session.secret()))
+                .addListener(f -> {
                     sendReadyForQuery(channel, TransactionState.IDLE);
                     if (properties.containsKey("CrateDBTransport")) {
                         switchToTransportProtocol(channel);

```

Generated
```diff
@@ -479,9 +459,9 @@
                 applyOptions(options);
             }
             Messages.sendAuthenticationOK(channel)
-                .addListener(_ -> sendParams(channel, session.sessionSettings()))
-                .addListener(_ -> Messages.sendKeyData(channel, session.id(), session.secret()))
-                .addListener(_ -> {
+                .addListener(f -> sendParams(channel, session.sessionSettings()))
+                .addListener(f -> Messages.sendKeyData(channel, session.id(), session.secret()))
+                .addListener(f -> {
                     sendReadyForQuery(channel, TransactionState.IDLE);
                     if (properties.containsKey("CrateDBTransport")) {
                         switchToTransportProtocol(channel);

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 11

Developer
```diff
@@ -704,7 +684,7 @@
      * | string portalName
      * | int32 maxRows (0 = unlimited)
      */
-    private void handleExecute(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+    private void handleExecute(ByteBuf buffer, DelayableWriteChannel channel) {
         String portalName = readCString(buffer);
         int maxRows = buffer.readInt();
         String query = session.getQuery(portalName);

```

Generated
```diff
@@ -704,7 +684,7 @@
      * | string portalName
      * | int32 maxRows (0 = unlimited)
      */
-    private void handleExecute(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+    private void handleExecute(ByteBuf buffer, DelayableWriteChannel channel) {
         String portalName = readCString(buffer);
         int maxRows = buffer.readInt();
         String query = session.getQuery(portalName);

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 12

Developer
```diff
@@ -715,6 +695,25 @@
             return;
         }
         List<? extends DataType<?>> outputTypes = session.getOutputTypes(portalName);
+
+        // .execute is going async and may execute the query in another thread-pool.
+        // The results are later sent to the clients via the `ResultReceiver` created
+        // above, The `channel.write` calls - which the `ResultReceiver` makes - may
+        // happen in a thread which is *not* a netty thread.
+        // If that is the case, netty schedules the writes instead of running them
+        // immediately. A consequence of that is that *this* thread can continue
+        // processing other messages from the client, and if this thread then sends messages to the
+        // client, these are sent immediately, overtaking the result messages of the
+        // execute that is triggered here.
+        //
+        // This would lead to out-of-order messages. For example, we could send a
+        // `parseComplete` before the `commandComplete` of the previous statement has
+        // been transmitted.
+        //
+        // To ensure clients receive messages in the correct order we delay all writes
+        // The "finish" logic of the ResultReceivers writes out all pending writes/unblocks the channel
+
+        DelayedWrites delayedWrites = channel.delayWrites();
         ResultReceiver<?> resultReceiver;
         if (outputTypes == null) {
             // this is a DML query

```

Generated
```diff
@@ -715,6 +695,25 @@
             return;
         }
         List<? extends DataType<?>> outputTypes = session.getOutputTypes(portalName);
+
+        // .execute is going async and may execute the query in another thread-pool.
+        // The results are later sent to the clients via the `ResultReceiver` created
+        // above, The `channel.write` calls - which the `ResultReceiver` makes - may
+        // happen in a thread which is *not* a netty thread.
+        // If that is the case, netty schedules the writes instead of running them
+        // immediately. A consequence of that is that *this* thread can continue
+        // processing other messages from the client, and if this thread then sends messages to the
+        // client, these are sent immediately, overtaking the result messages of the
+        // execute that is triggered here.
+        //
+        // This would lead to out-of-order messages. For example, we could send a
+        // `parseComplete` before the `commandComplete` of the previous statement has
+        // been transmitted.
+        //
+        // To ensure clients receive messages in the correct order we delay all writes
+        // The "finish" logic of the ResultReceivers writes out all pending writes/unblocks the channel
+
+        DelayedWrites delayedWrites = channel.delayWrites();
         ResultReceiver<?> resultReceiver;
         if (outputTypes == null) {
             // this is a DML query

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 13

Developer
```diff
@@ -722,6 +721,7 @@
             resultReceiver = new RowCountReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings())
             );
         } else {

```

Generated
```diff
@@ -722,6 +721,7 @@
             resultReceiver = new RowCountReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings())
             );
         } else {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 14

Developer
```diff
@@ -729,21 +729,16 @@
             resultReceiver = new ResultSetReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings()),
                 Lists.map(outputTypes, PGTypes::get),
                 session.getResultFormatCodes(portalName)
             );
         }
-        @Nullable
-        CompletableFuture<?> pendingExecution = session.execute(portalName, maxRows, resultReceiver);
-        if (pendingExecution == null) {
-            ctx.read();
-        } else {
-            pendingExecution.whenComplete((_, _) -> ctx.read());
-        }
+        session.execute(portalName, maxRows, resultReceiver);
     }
 
-    private void handleSync(ChannelHandlerContext ctx, Channel channel) {
+    private void handleSync(DelayableWriteChannel channel) {
         if (ignoreTillSync) {
             ignoreTillSync = false;
             // If an error happens all sub-sequent messages can be ignored until the client sends a sync message

```

Generated
```diff
@@ -729,21 +729,16 @@
             resultReceiver = new ResultSetReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings()),
                 Lists.map(outputTypes, PGTypes::get),
                 session.getResultFormatCodes(portalName)
             );
         }
-        @Nullable
-        CompletableFuture<?> pendingExecution = session.execute(portalName, maxRows, resultReceiver);
-        if (pendingExecution == null) {
-            ctx.read();
-        } else {
-            pendingExecution.whenComplete((_, _) -> ctx.read());
-        }
+        session.execute(portalName, maxRows, resultReceiver);
     }
 
-    private void handleSync(ChannelHandlerContext ctx, Channel channel) {
+    private void handleSync(DelayableWriteChannel channel) {
         if (ignoreTillSync) {
             ignoreTillSync = false;
             // If an error happens all sub-sequent messages can be ignored until the client sends a sync message

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 15

Developer
```diff
@@ -756,17 +751,17 @@
             //  4) p, b, e    -> We've a new query deferred.
             //  5) `sync`     -> We must execute the query from 4, but not 1)
             session.resetDeferredExecutions();
+            channel.writePendingMessages();
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
             return;
         }
         try {
-            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(ctx::read, channel, session.transactionState());
+            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(channel, session.transactionState());
             session.sync(false).whenComplete(readyForQueryCallback);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), t);
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
         }
     }
 

```

Generated
```diff
@@ -756,17 +751,17 @@
             //  4) p, b, e    -> We've a new query deferred.
             //  5) `sync`     -> We must execute the query from 4, but not 1)
             session.resetDeferredExecutions();
+            channel.writePendingMessages();
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
             return;
         }
         try {
-            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(ctx::read, channel, session.transactionState());
+            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(channel, session.transactionState());
             session.sync(false).whenComplete(readyForQueryCallback);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), t);
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
         }
     }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 16

Developer
```diff
@@ -781,7 +776,7 @@
     }
 
     @VisibleForTesting
-    void handleSimpleQuery(Runnable read, ByteBuf buffer, final Channel channel) {
+    void handleSimpleQuery(ByteBuf buffer, final DelayableWriteChannel channel) {
         assert session != null : "Session must be created when running a simple query";
         Session.TimeoutToken timeoutToken = session.newTimeoutToken();
         String queryString = readCString(buffer);

```

Generated
```diff
@@ -781,7 +776,7 @@
     }
 
     @VisibleForTesting
-    void handleSimpleQuery(Runnable read, ByteBuf buffer, final Channel channel) {
+    void handleSimpleQuery(ByteBuf buffer, final DelayableWriteChannel channel) {
         assert session != null : "Session must be created when running a simple query";
         Session.TimeoutToken timeoutToken = session.newTimeoutToken();
         String queryString = readCString(buffer);

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 17

Developer
```diff
@@ -799,7 +794,6 @@
         } catch (Exception ex) {
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), ex);
             sendReadyForQuery(channel, TransactionState.IDLE);
-            read.run();
             return;
         }
         timeoutToken.check();

```

Generated
```diff
@@ -799,7 +794,6 @@
         } catch (Exception ex) {
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), ex);
             sendReadyForQuery(channel, TransactionState.IDLE);
-            read.run();
             return;
         }
         timeoutToken.check();

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 18

Developer
```diff
@@ -807,12 +801,12 @@
         for (var statement : statements) {
             composedFuture = composedFuture.thenCompose(result -> handleSingleQuery(statement, queryString, channel, timeoutToken));
         }
-        composedFuture.whenComplete(new ReadyForQueryCallback(read, channel, TransactionState.IDLE));
+        composedFuture.whenComplete(new ReadyForQueryCallback(channel, TransactionState.IDLE));
     }
 
     private CompletableFuture<?> handleSingleQuery(Statement statement,
                                                    String query,
-                                                   Channel channel,
+                                                   DelayableWriteChannel channel,
                                                    Session.TimeoutToken timeoutToken) {
         CompletableFuture<?> result = new CompletableFuture<>();
 

```

Generated
```diff
@@ -807,12 +801,12 @@
         for (var statement : statements) {
             composedFuture = composedFuture.thenCompose(result -> handleSingleQuery(statement, queryString, channel, timeoutToken));
         }
-        composedFuture.whenComplete(new ReadyForQueryCallback(read, channel, TransactionState.IDLE));
+        composedFuture.whenComplete(new ReadyForQueryCallback(channel, TransactionState.IDLE));
     }
 
     private CompletableFuture<?> handleSingleQuery(Statement statement,
                                                    String query,
-                                                   Channel channel,
+                                                   DelayableWriteChannel channel,
                                                    Session.TimeoutToken timeoutToken) {
         CompletableFuture<?> result = new CompletableFuture<>();
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 19

Developer
```diff
@@ -831,17 +825,21 @@
             List<Symbol> fields = describeResult.getFields();
 
             if (fields == null) {
+                DelayedWrites delayedWrites = channel.delayWrites();
                 RowCountReceiver rowCountReceiver = new RowCountReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl
                 );
                 session.execute("", 0, rowCountReceiver);
             } else {
                 Messages.sendRowDescription(channel, fields, null, describeResult.relation());
+                DelayedWrites delayedWrites = channel.delayWrites();
                 ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl,
                     Lists.map(fields, x -> PGTypes.get(x.valueType())),
                     null

```

Generated
```diff
@@ -831,17 +825,21 @@
             List<Symbol> fields = describeResult.getFields();
 
             if (fields == null) {
+                DelayedWrites delayedWrites = channel.delayWrites();
                 RowCountReceiver rowCountReceiver = new RowCountReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl
                 );
                 session.execute("", 0, rowCountReceiver);
             } else {
                 Messages.sendRowDescription(channel, fields, null, describeResult.relation());
+                DelayedWrites delayedWrites = channel.delayWrites();
                 ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl,
                     Lists.map(fields, x -> PGTypes.get(x.valueType())),
                     null

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 20

Developer
```diff
@@ -850,6 +848,7 @@
             }
             return session.sync(false);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, accessControl, t);
             result.completeExceptionally(t);
             return result;

```

Generated
```diff
@@ -850,6 +848,7 @@
             }
             return session.sync(false);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, accessControl, t);
             result.completeExceptionally(t);
             return result;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java

- Developer hunks: 5
- Generated hunks: 5

#### Hunk 1

Developer
```diff
@@ -29,6 +29,7 @@
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.session.BaseResultReceiver;
 import io.netty.channel.Channel;

```

Generated
```diff
@@ -29,6 +29,7 @@
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.session.BaseResultReceiver;
 import io.netty.channel.Channel;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -37,9 +38,11 @@
 class ResultSetReceiver extends BaseResultReceiver {
 
     private final String query;
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final List<PGType<?>> columnTypes;
     private final AccessControl accessControl;
+    private final Channel directChannel;
+    private final DelayedWrites delayedWrites;
 
     @Nullable
     private final FormatCodes.FormatCode[] formatCodes;

```

Generated
```diff
@@ -37,9 +38,11 @@
 class ResultSetReceiver extends BaseResultReceiver {
 
     private final String query;
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final List<PGType<?>> columnTypes;
     private final AccessControl accessControl;
+    private final Channel directChannel;
+    private final DelayedWrites delayedWrites;
 
     @Nullable
     private final FormatCodes.FormatCode[] formatCodes;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 3

Developer
```diff
@@ -47,12 +50,15 @@
     private long rowCount = 0;
 
     ResultSetReceiver(String query,
-                      Channel channel,
+                      DelayableWriteChannel channel,
+                      DelayedWrites delayedWrites,
                       AccessControl accessControl,
                       List<PGType<?>> columnTypes,
                       @Nullable FormatCodes.FormatCode[] formatCodes) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
+        this.directChannel = channel.bypassDelay();
         this.accessControl = accessControl;
         this.columnTypes = columnTypes;
         this.formatCodes = formatCodes;

```

Generated
```diff
@@ -47,12 +50,15 @@
     private long rowCount = 0;
 
     ResultSetReceiver(String query,
-                      Channel channel,
+                      DelayableWriteChannel channel,
+                      DelayedWrites delayedWrites,
                       AccessControl accessControl,
                       List<PGType<?>> columnTypes,
                       @Nullable FormatCodes.FormatCode[] formatCodes) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
+        this.directChannel = channel.bypassDelay();
         this.accessControl = accessControl;
         this.columnTypes = columnTypes;
         this.formatCodes = formatCodes;

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 4

Developer
```diff
@@ -67,9 +73,9 @@
     @Nullable
     public CompletableFuture<Void> setNextRow(Row row) {
         rowCount++;
-        ChannelFuture sendDataRow = Messages.sendDataRow(channel, row, columnTypes, formatCodes);
+        ChannelFuture sendDataRow = Messages.sendDataRow(directChannel, row, columnTypes, formatCodes);
         CompletableFuture<Void> future;
-        boolean isWritable = channel.isWritable();
+        boolean isWritable = directChannel.isWritable();
         if (isWritable) {
             future = null;
         } else {

```

Generated
```diff
@@ -67,9 +73,9 @@
     @Nullable
     public CompletableFuture<Void> setNextRow(Row row) {
         rowCount++;
-        ChannelFuture sendDataRow = Messages.sendDataRow(channel, row, columnTypes, formatCodes);
+        ChannelFuture sendDataRow = Messages.sendDataRow(directChannel, row, columnTypes, formatCodes);
         CompletableFuture<Void> future;
-        boolean isWritable = channel.isWritable();
+        boolean isWritable = directChannel.isWritable();
         if (isWritable) {
             future = null;
         } else {

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 5

Developer
```diff
@@ -89,33 +95,36 @@
         // Flush the channel only every 1000 rows for better performance.
         // But flushing must be forced once the channel outbound buffer is full (= channel not in writable state)
         if (isWritable == false || rowCount % 1000 == 0) {
-            channel.flush();
+            directChannel.flush();
         }
         return future;
     }
 
     @Override
     public void batchFinished() {
-        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(channel);
+        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(directChannel);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
 
         // Trigger the completion future but by-pass `sendCompleteComplete`
         // This resultReceiver shouldn't be used anymore. The next `execute` message
         // from the client will create a new one.
-        sendPortalSuspended.addListener(_ -> super.allFinished());
+        sendPortalSuspended.addListener(f -> super.allFinished());
     }
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(directChannel, query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(directChannel, accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }

```

Generated
```diff
@@ -89,33 +95,36 @@
         // Flush the channel only every 1000 rows for better performance.
         // But flushing must be forced once the channel outbound buffer is full (= channel not in writable state)
         if (isWritable == false || rowCount % 1000 == 0) {
-            channel.flush();
+            directChannel.flush();
         }
         return future;
     }
 
     @Override
     public void batchFinished() {
-        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(channel);
+        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(directChannel);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
 
         // Trigger the completion future but by-pass `sendCompleteComplete`
         // This resultReceiver shouldn't be used anymore. The next `execute` message
         // from the client will create a new one.
-        sendPortalSuspended.addListener(_ -> super.allFinished());
+        sendPortalSuspended.addListener(f -> super.allFinished());
     }
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(directChannel, query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(directChannel, accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java

- Developer hunks: 2
- Generated hunks: 2

#### Hunk 1

Developer
```diff
@@ -26,24 +26,27 @@
 import org.jetbrains.annotations.NotNull;
 import org.jetbrains.annotations.Nullable;
 
+import io.crate.session.BaseResultReceiver;
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
-import io.crate.session.BaseResultReceiver;
-import io.netty.channel.Channel;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.netty.channel.ChannelFuture;
 
 class RowCountReceiver extends BaseResultReceiver {
 
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final String query;
     private final AccessControl accessControl;
+    private final DelayedWrites delayedWrites;
     private long rowCount;
 
     RowCountReceiver(String query,
-                     Channel channel,
+                     DelayableWriteChannel channel,
+                     DelayedWrites delayedWrites,
                      AccessControl accessControl) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
         this.accessControl = accessControl;
     }
 

```

Generated
```diff
@@ -26,24 +26,27 @@
 import org.jetbrains.annotations.NotNull;
 import org.jetbrains.annotations.Nullable;
 
+import io.crate.session.BaseResultReceiver;
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
-import io.crate.session.BaseResultReceiver;
-import io.netty.channel.Channel;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.netty.channel.ChannelFuture;
 
 class RowCountReceiver extends BaseResultReceiver {
 
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final String query;
     private final AccessControl accessControl;
+    private final DelayedWrites delayedWrites;
     private long rowCount;
 
     RowCountReceiver(String query,
-                     Channel channel,
+                     DelayableWriteChannel channel,
+                     DelayedWrites delayedWrites,
                      AccessControl accessControl) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
         this.accessControl = accessControl;
     }
 

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -63,15 +66,17 @@
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel.bypassDelay(), query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel.bypassDelay(), accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }

```

Generated
```diff
@@ -63,15 +66,17 @@
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel.bypassDelay(), query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel.bypassDelay(), accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```


### server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java

- Developer hunks: 2
- Generated hunks: 2

#### Hunk 1

Developer
```diff
@@ -277,8 +277,7 @@
             maybeInjectSSL(ch);
             ch.pipeline().addLast("logging", loggingHandler);
             // using a dot as a prefix means this cannot come from any settings parsed
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```

Generated
```diff
@@ -277,8 +277,7 @@
             maybeInjectSSL(ch);
             ch.pipeline().addLast("logging", loggingHandler);
             // using a dot as a prefix means this cannot come from any settings parsed
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```

#### Hunk 2

Developer
```diff
@@ -320,8 +319,7 @@
             ch.attr(CHANNEL_KEY).set(nettyTcpChannel);
             serverAcceptedChannel(nettyTcpChannel);
             ch.pipeline().addLast("logging", loggingHandler);
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```

Generated
```diff
@@ -320,8 +319,7 @@
             ch.attr(CHANNEL_KEY).set(nettyTcpChannel);
             serverAcceptedChannel(nettyTcpChannel);
             ch.pipeline().addLast("logging", loggingHandler);
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```

Developer -> Generated (Unified Diff)
```diff
(No textual difference)

```



## Full Generated Patch (Agent-Only, code-only)
```diff
diff --git a/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
new file mode 100644
index 0000000000..6816d8ef26
--- /dev/null
+++ b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
@@ -0,0 +1,352 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import java.net.SocketAddress;
+import java.util.ArrayDeque;
+
+import org.jetbrains.annotations.Nullable;
+
+import io.netty.buffer.ByteBufAllocator;
+import io.netty.channel.Channel;
+import io.netty.channel.ChannelConfig;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelId;
+import io.netty.channel.ChannelMetadata;
+import io.netty.channel.ChannelPipeline;
+import io.netty.channel.ChannelProgressivePromise;
+import io.netty.channel.ChannelPromise;
+import io.netty.channel.EventLoop;
+import io.netty.util.Attribute;
+import io.netty.util.AttributeKey;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * Channel implementation that allows to delay writes with `blockWritesUntil`
+ **/
+public class DelayableWriteChannel implements Channel {
+
+    private final Channel delegate;
+    private DelayedWrites delay = null;
+
+    public DelayableWriteChannel(Channel channel) {
+        this.delegate = channel;
+        channel.closeFuture().addListener(_ -> discardDelayedWrites());
+    }
+
+    @Override
+    public <T> Attribute<T> attr(AttributeKey<T> key) {
+        return delegate.attr(key);
+    }
+
+    @Override
+    public <T> boolean hasAttr(AttributeKey<T> key) {
+        return delegate.hasAttr(key);
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress) {
+        return delegate.bind(localAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress) {
+        return delegate.connect(remoteAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress) {
+        return delegate.connect(remoteAddress, localAddress);
+    }
+
+    @Override
+    public ChannelFuture disconnect() {
+        return delegate.disconnect();
+    }
+
+    @Override
+    public ChannelFuture close() {
+        return delegate.close();
+    }
+
+    @Override
+    public ChannelFuture deregister() {
+        return delegate.deregister();
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.bind(localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture disconnect(ChannelPromise promise) {
+        return delegate.disconnect(promise);
+    }
+
+    @Override
+    public ChannelFuture close(ChannelPromise promise) {
+        return delegate.close(promise);
+    }
+
+    @Override
+    public ChannelFuture deregister(ChannelPromise promise) {
+        return delegate.deregister(promise);
+    }
+
+    @Override
+    public ChannelFuture write(Object msg) {
+        return this.write(msg, newPromise());
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg) {
+        return this.writeAndFlush(msg, newPromise());
+    }
+
+    @Override
+    public ChannelPromise newPromise() {
+        return delegate.newPromise();
+    }
+
+    @Override
+    public ChannelProgressivePromise newProgressivePromise() {
+        return delegate.newProgressivePromise();
+    }
+
+    @Override
+    public ChannelFuture newSucceededFuture() {
+        return delegate.newSucceededFuture();
+    }
+
+    @Override
+    public ChannelFuture newFailedFuture(Throwable cause) {
+        return delegate.newFailedFuture(cause);
+    }
+
+    @Override
+    public ChannelPromise voidPromise() {
+        return delegate.voidPromise();
+    }
+
+    @Override
+    public int compareTo(Channel o) {
+        return delegate.compareTo(o);
+    }
+
+    @Override
+    public ChannelId id() {
+        return delegate.id();
+    }
+
+    @Override
+    public EventLoop eventLoop() {
+        return delegate.eventLoop();
+    }
+
+    @Override
+    public Channel parent() {
+        return delegate.parent();
+    }
+
+    @Override
+    public ChannelConfig config() {
+        return delegate.config();
+    }
+
+    @Override
+    public boolean isOpen() {
+        return delegate.isOpen();
+    }
+
+    @Override
+    public boolean isRegistered() {
+        return delegate.isRegistered();
+    }
+
+    @Override
+    public boolean isActive() {
+        return delegate.isActive();
+    }
+
+    @Override
+    public ChannelMetadata metadata() {
+        return delegate.metadata();
+    }
+
+    @Override
+    public SocketAddress localAddress() {
+        return delegate.localAddress();
+    }
+
+    @Override
+    public SocketAddress remoteAddress() {
+        return delegate.remoteAddress();
+    }
+
+    @Override
+    public ChannelFuture closeFuture() {
+        return delegate.closeFuture();
+    }
+
+    @Override
+    public boolean isWritable() {
+        return delegate.isWritable();
+    }
+
+    @Override
+    public long bytesBeforeUnwritable() {
+        return delegate.bytesBeforeUnwritable();
+    }
+
+    @Override
+    public long bytesBeforeWritable() {
+        return delegate.bytesBeforeWritable();
+    }
+
+    @Override
+    public Unsafe unsafe() {
+        return delegate.unsafe();
+    }
+
+    @Override
+    public ChannelPipeline pipeline() {
+        return delegate.pipeline();
+    }
+
+    @Override
+    public ByteBufAllocator alloc() {
+        return delegate.alloc();
+    }
+
+    @Override
+    public Channel read() {
+        return delegate.read();
+    }
+
+    @Override
+    public Channel flush() {
+        return delegate.flush();
+    }
+
+    public Channel bypassDelay() {
+        return delegate;
+    }
+
+
+    @Override
+    public ChannelFuture write(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.write(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.write(msg, promise);
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.writeAndFlush(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.writeAndFlush(msg, promise);
+    }
+
+    public synchronized void discardDelayedWrites() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.discard();
+                parent = parent.parent;
+            }
+            delay.discard();
+            delay = null;
+        }
+    }
+
+    public synchronized void writePendingMessages(DelayedWrites delayedWrites) {
+        if (delay == delayedWrites) {
+            delay = null;
+        }
+        delayedWrites.writeDelayed();
+    }
+
+    public synchronized void writePendingMessages() {
+        if (delay == null) {
+            return;
+        }
+        DelayedWrites delayedWrites = delay;
+        delay = null;
+        delayedWrites.writeDelayed();
+    }
+
+    public DelayedWrites delayWrites() {
+        DelayedWrites delayedWrites = new DelayedWrites(delay);
+        delay = delayedWrites;
+        return delayedWrites;
+    }
+
+    record DelayedMsg(Object msg, Runnable runnable) {
+    }
+
+    static class DelayedWrites {
+
+        private final ArrayDeque<DelayedMsg> delayed = new ArrayDeque<>();
+        private final DelayedWrites parent;
+
+        public DelayedWrites(@Nullable DelayedWrites parent) {
+            this.parent = parent;
+        }
+
+        public void discard() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                ReferenceCountUtil.safeRelease(delayedMsg.msg);
+            }
+        }
+
+        public void add(Object msg, Runnable runnable) {
+            delayed.add(new DelayedMsg(msg, runnable));
+        }
+
+        private void writeDelayed() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                delayedMsg.runnable.run();
+            }
+        }
+    }
+}
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
index b596538315..30199e1288 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
@@ -70,7 +70,6 @@ import io.crate.types.DataTypes;
 import io.netty.bootstrap.ServerBootstrap;
 import io.netty.channel.Channel;
 import io.netty.channel.ChannelInitializer;
-import io.netty.channel.ChannelOption;
 import io.netty.channel.ChannelPipeline;
 import io.netty.handler.ssl.SslContext;
 
@@ -168,7 +167,6 @@ public class PostgresNetty extends AbstractLifecycleComponent {
         }
         var eventLoopGroup = nettyBootstrap.getSharedEventLoopGroup();
         bootstrap = NettyBootstrap.newServerBootstrap(settings, eventLoopGroup);
-        bootstrap.childOption(ChannelOption.AUTO_READ, false);
         inboundStatsHandler = new Netty4InboundStatsHandler(statsTracker, LOGGER);
         outboundStatsHandler = new Netty4OutboundStatsHandler(statsTracker, LOGGER);
 
@@ -189,8 +187,7 @@ public class PostgresNetty extends AbstractLifecycleComponent {
                     chPipeline -> {
                         var nettyTcpChannel = new CloseableChannel(ch, true);
                         ch.attr(Netty4Transport.CHANNEL_KEY).set(nettyTcpChannel);
-                        var handler = new Netty4MessageChannelHandler(pageCacheRecycler, transport, false);
-                        chPipeline.addLast("dispatcher", handler);
+                        chPipeline.addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, transport));
                     },
                     authentication,
                     sslContextProvider
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index e016fbc588..9f7aff8974 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -61,6 +61,7 @@ import io.crate.expression.symbol.Symbol;
 import io.crate.metadata.settings.CoordinatorSessionSettings;
 import io.crate.metadata.settings.session.SessionSetting;
 import io.crate.metadata.settings.session.SessionSettingRegistry;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.role.Role;
@@ -205,7 +206,7 @@ public class PostgresWireProtocol {
     private final Authentication authService;
     private final Consumer<ChannelPipeline> addTransportHandler;
 
-    private Channel channel;
+    private DelayableWriteChannel channel;
     Session session;
     private boolean ignoreTillSync = false;
     private AuthenticationContext authContext;
@@ -265,10 +266,8 @@ public class PostgresWireProtocol {
     private static class ReadyForQueryCallback implements BiConsumer<Object, Throwable> {
         private final Channel channel;
         private final TransactionState transactionState;
-        private final Runnable read;
 
-        private ReadyForQueryCallback(Runnable read, Channel channel, TransactionState transactionState) {
-            this.read = read;
+        private ReadyForQueryCallback(Channel channel, TransactionState transactionState) {
             this.channel = channel;
             this.transactionState = transactionState;
         }
@@ -276,7 +275,6 @@ public class PostgresWireProtocol {
         @Override
         public void accept(Object result, Throwable t) {
             sendReadyForQuery(channel, transactionState);
-            read.run();
         }
     }
 
@@ -284,7 +282,7 @@ public class PostgresWireProtocol {
 
         @Override
         public void channelRegistered(ChannelHandlerContext ctx) throws Exception {
-            channel = ctx.channel();
+            channel = new DelayableWriteChannel(ctx.channel());
         }
 
         @Override
@@ -292,17 +290,11 @@ public class PostgresWireProtocol {
             return true;
         }
 
-        @Override
-        public void channelActive(ChannelHandlerContext ctx) throws Exception {
-            super.channelActive(ctx);
-            ctx.read();
-        }
-
         @Override
         public void channelRead0(ChannelHandlerContext ctx, ByteBuf buffer) throws Exception {
             assert channel != null : "Channel must be initialized";
             try {
-                dispatchState(ctx, buffer, channel);
+                dispatchState(buffer, channel);
             } catch (Throwable t) {
                 ignoreTillSync = true;
                 try {
@@ -313,21 +305,18 @@ public class PostgresWireProtocol {
                 } catch (Throwable ti) {
                     LOGGER.error("Error trying to send error to client: {}", t, ti);
                 }
-                ctx.read();
             }
         }
 
-        private void dispatchState(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchState(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.state()) {
                 case STARTUP_PARAMETERS:
                     handleStartupBody(buffer, channel);
                     decoder.startupDone();
-                    ctx.read();
                     return;
 
                 case CANCEL:
                     handleCancelRequestBody(buffer, channel);
-                    ctx.read();
                     return;
 
                 case MSG:
@@ -335,55 +324,47 @@ public class PostgresWireProtocol {
 
                     if (ignoreTillSync && decoder.msgType() != 'S') {
                         buffer.skipBytes(decoder.payloadLength());
-                        ctx.read();
                         return;
                     }
-                    dispatchMessage(ctx, buffer, channel);
+                    dispatchMessage(buffer, channel);
                     return;
                 default:
                     throw new IllegalStateException("Illegal state: " + decoder.state());
             }
         }
 
-        private void dispatchMessage(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchMessage(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.msgType()) {
                 case 'Q': // Query (simple)
-                    handleSimpleQuery(ctx::read, buffer, channel);
+                    handleSimpleQuery(buffer, channel);
                     return;
                 case 'P':
                     handleParseMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'p':
                     handlePassword(buffer, channel);
-                    ctx.read();
                     return;
                 case 'B':
                     handleBindMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'D':
                     handleDescribeMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'E':
-                    handleExecute(ctx, buffer, channel);
+                    handleExecute(buffer, channel);
                     return;
                 case 'H':
                     handleFlush(channel);
-                    ctx.read();
                     return;
                 case 'S':
-                    handleSync(ctx, channel);
+                    handleSync(channel);
                     return;
                 case 'C':
                     handleClose(buffer, channel);
-                    ctx.read();
                     return;
                 case 'X': // Terminate (called when jdbc connection is closed)
                     closeSession();
                     channel.close();
-                    ctx.read();
                     return;
                 default:
                     Messages.sendErrorResponse(
@@ -392,7 +373,6 @@ public class PostgresWireProtocol {
                             ? AccessControl.DISABLED
                             : getAccessControl.apply(session.sessionSettings()),
                         new UnsupportedOperationException("Unsupported messageType: " + decoder.msgType()));
-                    ctx.read();
             }
         }
 
@@ -479,9 +459,9 @@ public class PostgresWireProtocol {
                 applyOptions(options);
             }
             Messages.sendAuthenticationOK(channel)
-                .addListener(_ -> sendParams(channel, session.sessionSettings()))
-                .addListener(_ -> Messages.sendKeyData(channel, session.id(), session.secret()))
-                .addListener(_ -> {
+                .addListener(f -> sendParams(channel, session.sessionSettings()))
+                .addListener(f -> Messages.sendKeyData(channel, session.id(), session.secret()))
+                .addListener(f -> {
                     sendReadyForQuery(channel, TransactionState.IDLE);
                     if (properties.containsKey("CrateDBTransport")) {
                         switchToTransportProtocol(channel);
@@ -704,7 +684,7 @@ public class PostgresWireProtocol {
      * | string portalName
      * | int32 maxRows (0 = unlimited)
      */
-    private void handleExecute(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+    private void handleExecute(ByteBuf buffer, DelayableWriteChannel channel) {
         String portalName = readCString(buffer);
         int maxRows = buffer.readInt();
         String query = session.getQuery(portalName);
@@ -715,6 +695,25 @@ public class PostgresWireProtocol {
             return;
         }
         List<? extends DataType<?>> outputTypes = session.getOutputTypes(portalName);
+
+        // .execute is going async and may execute the query in another thread-pool.
+        // The results are later sent to the clients via the `ResultReceiver` created
+        // above, The `channel.write` calls - which the `ResultReceiver` makes - may
+        // happen in a thread which is *not* a netty thread.
+        // If that is the case, netty schedules the writes instead of running them
+        // immediately. A consequence of that is that *this* thread can continue
+        // processing other messages from the client, and if this thread then sends messages to the
+        // client, these are sent immediately, overtaking the result messages of the
+        // execute that is triggered here.
+        //
+        // This would lead to out-of-order messages. For example, we could send a
+        // `parseComplete` before the `commandComplete` of the previous statement has
+        // been transmitted.
+        //
+        // To ensure clients receive messages in the correct order we delay all writes
+        // The "finish" logic of the ResultReceivers writes out all pending writes/unblocks the channel
+
+        DelayedWrites delayedWrites = channel.delayWrites();
         ResultReceiver<?> resultReceiver;
         if (outputTypes == null) {
             // this is a DML query
@@ -722,6 +721,7 @@ public class PostgresWireProtocol {
             resultReceiver = new RowCountReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings())
             );
         } else {
@@ -729,21 +729,16 @@ public class PostgresWireProtocol {
             resultReceiver = new ResultSetReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings()),
                 Lists.map(outputTypes, PGTypes::get),
                 session.getResultFormatCodes(portalName)
             );
         }
-        @Nullable
-        CompletableFuture<?> pendingExecution = session.execute(portalName, maxRows, resultReceiver);
-        if (pendingExecution == null) {
-            ctx.read();
-        } else {
-            pendingExecution.whenComplete((_, _) -> ctx.read());
-        }
+        session.execute(portalName, maxRows, resultReceiver);
     }
 
-    private void handleSync(ChannelHandlerContext ctx, Channel channel) {
+    private void handleSync(DelayableWriteChannel channel) {
         if (ignoreTillSync) {
             ignoreTillSync = false;
             // If an error happens all sub-sequent messages can be ignored until the client sends a sync message
@@ -756,17 +751,17 @@ public class PostgresWireProtocol {
             //  4) p, b, e    -> We've a new query deferred.
             //  5) `sync`     -> We must execute the query from 4, but not 1)
             session.resetDeferredExecutions();
+            channel.writePendingMessages();
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
             return;
         }
         try {
-            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(ctx::read, channel, session.transactionState());
+            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(channel, session.transactionState());
             session.sync(false).whenComplete(readyForQueryCallback);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), t);
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
         }
     }
 
@@ -781,7 +776,7 @@ public class PostgresWireProtocol {
     }
 
     @VisibleForTesting
-    void handleSimpleQuery(Runnable read, ByteBuf buffer, final Channel channel) {
+    void handleSimpleQuery(ByteBuf buffer, final DelayableWriteChannel channel) {
         assert session != null : "Session must be created when running a simple query";
         Session.TimeoutToken timeoutToken = session.newTimeoutToken();
         String queryString = readCString(buffer);
@@ -799,7 +794,6 @@ public class PostgresWireProtocol {
         } catch (Exception ex) {
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), ex);
             sendReadyForQuery(channel, TransactionState.IDLE);
-            read.run();
             return;
         }
         timeoutToken.check();
@@ -807,12 +801,12 @@ public class PostgresWireProtocol {
         for (var statement : statements) {
             composedFuture = composedFuture.thenCompose(result -> handleSingleQuery(statement, queryString, channel, timeoutToken));
         }
-        composedFuture.whenComplete(new ReadyForQueryCallback(read, channel, TransactionState.IDLE));
+        composedFuture.whenComplete(new ReadyForQueryCallback(channel, TransactionState.IDLE));
     }
 
     private CompletableFuture<?> handleSingleQuery(Statement statement,
                                                    String query,
-                                                   Channel channel,
+                                                   DelayableWriteChannel channel,
                                                    Session.TimeoutToken timeoutToken) {
         CompletableFuture<?> result = new CompletableFuture<>();
 
@@ -831,17 +825,21 @@ public class PostgresWireProtocol {
             List<Symbol> fields = describeResult.getFields();
 
             if (fields == null) {
+                DelayedWrites delayedWrites = channel.delayWrites();
                 RowCountReceiver rowCountReceiver = new RowCountReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl
                 );
                 session.execute("", 0, rowCountReceiver);
             } else {
                 Messages.sendRowDescription(channel, fields, null, describeResult.relation());
+                DelayedWrites delayedWrites = channel.delayWrites();
                 ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl,
                     Lists.map(fields, x -> PGTypes.get(x.valueType())),
                     null
@@ -850,6 +848,7 @@ public class PostgresWireProtocol {
             }
             return session.sync(false);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, accessControl, t);
             result.completeExceptionally(t);
             return result;
diff --git a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
index d7a09fa191..9c6f657a6c 100644
--- a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
@@ -29,6 +29,7 @@ import org.jetbrains.annotations.Nullable;
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.session.BaseResultReceiver;
 import io.netty.channel.Channel;
@@ -37,9 +38,11 @@ import io.netty.channel.ChannelFuture;
 class ResultSetReceiver extends BaseResultReceiver {
 
     private final String query;
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final List<PGType<?>> columnTypes;
     private final AccessControl accessControl;
+    private final Channel directChannel;
+    private final DelayedWrites delayedWrites;
 
     @Nullable
     private final FormatCodes.FormatCode[] formatCodes;
@@ -47,12 +50,15 @@ class ResultSetReceiver extends BaseResultReceiver {
     private long rowCount = 0;
 
     ResultSetReceiver(String query,
-                      Channel channel,
+                      DelayableWriteChannel channel,
+                      DelayedWrites delayedWrites,
                       AccessControl accessControl,
                       List<PGType<?>> columnTypes,
                       @Nullable FormatCodes.FormatCode[] formatCodes) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
+        this.directChannel = channel.bypassDelay();
         this.accessControl = accessControl;
         this.columnTypes = columnTypes;
         this.formatCodes = formatCodes;
@@ -67,9 +73,9 @@ class ResultSetReceiver extends BaseResultReceiver {
     @Nullable
     public CompletableFuture<Void> setNextRow(Row row) {
         rowCount++;
-        ChannelFuture sendDataRow = Messages.sendDataRow(channel, row, columnTypes, formatCodes);
+        ChannelFuture sendDataRow = Messages.sendDataRow(directChannel, row, columnTypes, formatCodes);
         CompletableFuture<Void> future;
-        boolean isWritable = channel.isWritable();
+        boolean isWritable = directChannel.isWritable();
         if (isWritable) {
             future = null;
         } else {
@@ -89,33 +95,36 @@ class ResultSetReceiver extends BaseResultReceiver {
         // Flush the channel only every 1000 rows for better performance.
         // But flushing must be forced once the channel outbound buffer is full (= channel not in writable state)
         if (isWritable == false || rowCount % 1000 == 0) {
-            channel.flush();
+            directChannel.flush();
         }
         return future;
     }
 
     @Override
     public void batchFinished() {
-        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(channel);
+        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(directChannel);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
 
         // Trigger the completion future but by-pass `sendCompleteComplete`
         // This resultReceiver shouldn't be used anymore. The next `execute` message
         // from the client will create a new one.
-        sendPortalSuspended.addListener(_ -> super.allFinished());
+        sendPortalSuspended.addListener(f -> super.allFinished());
     }
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(directChannel, query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(directChannel, accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
index d752160edd..7ef1bdc276 100644
--- a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
@@ -26,24 +26,27 @@ import java.util.concurrent.CompletableFuture;
 import org.jetbrains.annotations.NotNull;
 import org.jetbrains.annotations.Nullable;
 
+import io.crate.session.BaseResultReceiver;
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
-import io.crate.session.BaseResultReceiver;
-import io.netty.channel.Channel;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.netty.channel.ChannelFuture;
 
 class RowCountReceiver extends BaseResultReceiver {
 
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final String query;
     private final AccessControl accessControl;
+    private final DelayedWrites delayedWrites;
     private long rowCount;
 
     RowCountReceiver(String query,
-                     Channel channel,
+                     DelayableWriteChannel channel,
+                     DelayedWrites delayedWrites,
                      AccessControl accessControl) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
         this.accessControl = accessControl;
     }
 
@@ -63,15 +66,17 @@ class RowCountReceiver extends BaseResultReceiver {
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel.bypassDelay(), query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel.bypassDelay(), accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
index 9dbb95487f..77cca1144d 100644
--- a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
+++ b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
@@ -277,8 +277,7 @@ public class Netty4Transport extends TcpTransport {
             maybeInjectSSL(ch);
             ch.pipeline().addLast("logging", loggingHandler);
             // using a dot as a prefix means this cannot come from any settings parsed
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override
@@ -320,8 +319,7 @@ public class Netty4Transport extends TcpTransport {
             ch.attr(CHANNEL_KEY).set(nettyTcpChannel);
             serverAcceptedChannel(nettyTcpChannel);
             ch.pipeline().addLast("logging", loggingHandler);
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```

## Full Generated Patch (Final Effective, code-only)
```diff
diff --git a/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
new file mode 100644
index 0000000000..6816d8ef26
--- /dev/null
+++ b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
@@ -0,0 +1,352 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import java.net.SocketAddress;
+import java.util.ArrayDeque;
+
+import org.jetbrains.annotations.Nullable;
+
+import io.netty.buffer.ByteBufAllocator;
+import io.netty.channel.Channel;
+import io.netty.channel.ChannelConfig;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelId;
+import io.netty.channel.ChannelMetadata;
+import io.netty.channel.ChannelPipeline;
+import io.netty.channel.ChannelProgressivePromise;
+import io.netty.channel.ChannelPromise;
+import io.netty.channel.EventLoop;
+import io.netty.util.Attribute;
+import io.netty.util.AttributeKey;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * Channel implementation that allows to delay writes with `blockWritesUntil`
+ **/
+public class DelayableWriteChannel implements Channel {
+
+    private final Channel delegate;
+    private DelayedWrites delay = null;
+
+    public DelayableWriteChannel(Channel channel) {
+        this.delegate = channel;
+        channel.closeFuture().addListener(_ -> discardDelayedWrites());
+    }
+
+    @Override
+    public <T> Attribute<T> attr(AttributeKey<T> key) {
+        return delegate.attr(key);
+    }
+
+    @Override
+    public <T> boolean hasAttr(AttributeKey<T> key) {
+        return delegate.hasAttr(key);
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress) {
+        return delegate.bind(localAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress) {
+        return delegate.connect(remoteAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress) {
+        return delegate.connect(remoteAddress, localAddress);
+    }
+
+    @Override
+    public ChannelFuture disconnect() {
+        return delegate.disconnect();
+    }
+
+    @Override
+    public ChannelFuture close() {
+        return delegate.close();
+    }
+
+    @Override
+    public ChannelFuture deregister() {
+        return delegate.deregister();
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.bind(localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture disconnect(ChannelPromise promise) {
+        return delegate.disconnect(promise);
+    }
+
+    @Override
+    public ChannelFuture close(ChannelPromise promise) {
+        return delegate.close(promise);
+    }
+
+    @Override
+    public ChannelFuture deregister(ChannelPromise promise) {
+        return delegate.deregister(promise);
+    }
+
+    @Override
+    public ChannelFuture write(Object msg) {
+        return this.write(msg, newPromise());
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg) {
+        return this.writeAndFlush(msg, newPromise());
+    }
+
+    @Override
+    public ChannelPromise newPromise() {
+        return delegate.newPromise();
+    }
+
+    @Override
+    public ChannelProgressivePromise newProgressivePromise() {
+        return delegate.newProgressivePromise();
+    }
+
+    @Override
+    public ChannelFuture newSucceededFuture() {
+        return delegate.newSucceededFuture();
+    }
+
+    @Override
+    public ChannelFuture newFailedFuture(Throwable cause) {
+        return delegate.newFailedFuture(cause);
+    }
+
+    @Override
+    public ChannelPromise voidPromise() {
+        return delegate.voidPromise();
+    }
+
+    @Override
+    public int compareTo(Channel o) {
+        return delegate.compareTo(o);
+    }
+
+    @Override
+    public ChannelId id() {
+        return delegate.id();
+    }
+
+    @Override
+    public EventLoop eventLoop() {
+        return delegate.eventLoop();
+    }
+
+    @Override
+    public Channel parent() {
+        return delegate.parent();
+    }
+
+    @Override
+    public ChannelConfig config() {
+        return delegate.config();
+    }
+
+    @Override
+    public boolean isOpen() {
+        return delegate.isOpen();
+    }
+
+    @Override
+    public boolean isRegistered() {
+        return delegate.isRegistered();
+    }
+
+    @Override
+    public boolean isActive() {
+        return delegate.isActive();
+    }
+
+    @Override
+    public ChannelMetadata metadata() {
+        return delegate.metadata();
+    }
+
+    @Override
+    public SocketAddress localAddress() {
+        return delegate.localAddress();
+    }
+
+    @Override
+    public SocketAddress remoteAddress() {
+        return delegate.remoteAddress();
+    }
+
+    @Override
+    public ChannelFuture closeFuture() {
+        return delegate.closeFuture();
+    }
+
+    @Override
+    public boolean isWritable() {
+        return delegate.isWritable();
+    }
+
+    @Override
+    public long bytesBeforeUnwritable() {
+        return delegate.bytesBeforeUnwritable();
+    }
+
+    @Override
+    public long bytesBeforeWritable() {
+        return delegate.bytesBeforeWritable();
+    }
+
+    @Override
+    public Unsafe unsafe() {
+        return delegate.unsafe();
+    }
+
+    @Override
+    public ChannelPipeline pipeline() {
+        return delegate.pipeline();
+    }
+
+    @Override
+    public ByteBufAllocator alloc() {
+        return delegate.alloc();
+    }
+
+    @Override
+    public Channel read() {
+        return delegate.read();
+    }
+
+    @Override
+    public Channel flush() {
+        return delegate.flush();
+    }
+
+    public Channel bypassDelay() {
+        return delegate;
+    }
+
+
+    @Override
+    public ChannelFuture write(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.write(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.write(msg, promise);
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.writeAndFlush(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.writeAndFlush(msg, promise);
+    }
+
+    public synchronized void discardDelayedWrites() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.discard();
+                parent = parent.parent;
+            }
+            delay.discard();
+            delay = null;
+        }
+    }
+
+    public synchronized void writePendingMessages(DelayedWrites delayedWrites) {
+        if (delay == delayedWrites) {
+            delay = null;
+        }
+        delayedWrites.writeDelayed();
+    }
+
+    public synchronized void writePendingMessages() {
+        if (delay == null) {
+            return;
+        }
+        DelayedWrites delayedWrites = delay;
+        delay = null;
+        delayedWrites.writeDelayed();
+    }
+
+    public DelayedWrites delayWrites() {
+        DelayedWrites delayedWrites = new DelayedWrites(delay);
+        delay = delayedWrites;
+        return delayedWrites;
+    }
+
+    record DelayedMsg(Object msg, Runnable runnable) {
+    }
+
+    static class DelayedWrites {
+
+        private final ArrayDeque<DelayedMsg> delayed = new ArrayDeque<>();
+        private final DelayedWrites parent;
+
+        public DelayedWrites(@Nullable DelayedWrites parent) {
+            this.parent = parent;
+        }
+
+        public void discard() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                ReferenceCountUtil.safeRelease(delayedMsg.msg);
+            }
+        }
+
+        public void add(Object msg, Runnable runnable) {
+            delayed.add(new DelayedMsg(msg, runnable));
+        }
+
+        private void writeDelayed() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                delayedMsg.runnable.run();
+            }
+        }
+    }
+}
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
index b596538315..30199e1288 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
@@ -70,7 +70,6 @@ import io.crate.types.DataTypes;
 import io.netty.bootstrap.ServerBootstrap;
 import io.netty.channel.Channel;
 import io.netty.channel.ChannelInitializer;
-import io.netty.channel.ChannelOption;
 import io.netty.channel.ChannelPipeline;
 import io.netty.handler.ssl.SslContext;
 
@@ -168,7 +167,6 @@ public class PostgresNetty extends AbstractLifecycleComponent {
         }
         var eventLoopGroup = nettyBootstrap.getSharedEventLoopGroup();
         bootstrap = NettyBootstrap.newServerBootstrap(settings, eventLoopGroup);
-        bootstrap.childOption(ChannelOption.AUTO_READ, false);
         inboundStatsHandler = new Netty4InboundStatsHandler(statsTracker, LOGGER);
         outboundStatsHandler = new Netty4OutboundStatsHandler(statsTracker, LOGGER);
 
@@ -189,8 +187,7 @@ public class PostgresNetty extends AbstractLifecycleComponent {
                     chPipeline -> {
                         var nettyTcpChannel = new CloseableChannel(ch, true);
                         ch.attr(Netty4Transport.CHANNEL_KEY).set(nettyTcpChannel);
-                        var handler = new Netty4MessageChannelHandler(pageCacheRecycler, transport, false);
-                        chPipeline.addLast("dispatcher", handler);
+                        chPipeline.addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, transport));
                     },
                     authentication,
                     sslContextProvider
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index e016fbc588..9f7aff8974 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -61,6 +61,7 @@ import io.crate.expression.symbol.Symbol;
 import io.crate.metadata.settings.CoordinatorSessionSettings;
 import io.crate.metadata.settings.session.SessionSetting;
 import io.crate.metadata.settings.session.SessionSettingRegistry;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.role.Role;
@@ -205,7 +206,7 @@ public class PostgresWireProtocol {
     private final Authentication authService;
     private final Consumer<ChannelPipeline> addTransportHandler;
 
-    private Channel channel;
+    private DelayableWriteChannel channel;
     Session session;
     private boolean ignoreTillSync = false;
     private AuthenticationContext authContext;
@@ -265,10 +266,8 @@ public class PostgresWireProtocol {
     private static class ReadyForQueryCallback implements BiConsumer<Object, Throwable> {
         private final Channel channel;
         private final TransactionState transactionState;
-        private final Runnable read;
 
-        private ReadyForQueryCallback(Runnable read, Channel channel, TransactionState transactionState) {
-            this.read = read;
+        private ReadyForQueryCallback(Channel channel, TransactionState transactionState) {
             this.channel = channel;
             this.transactionState = transactionState;
         }
@@ -276,7 +275,6 @@ public class PostgresWireProtocol {
         @Override
         public void accept(Object result, Throwable t) {
             sendReadyForQuery(channel, transactionState);
-            read.run();
         }
     }
 
@@ -284,7 +282,7 @@ public class PostgresWireProtocol {
 
         @Override
         public void channelRegistered(ChannelHandlerContext ctx) throws Exception {
-            channel = ctx.channel();
+            channel = new DelayableWriteChannel(ctx.channel());
         }
 
         @Override
@@ -292,17 +290,11 @@ public class PostgresWireProtocol {
             return true;
         }
 
-        @Override
-        public void channelActive(ChannelHandlerContext ctx) throws Exception {
-            super.channelActive(ctx);
-            ctx.read();
-        }
-
         @Override
         public void channelRead0(ChannelHandlerContext ctx, ByteBuf buffer) throws Exception {
             assert channel != null : "Channel must be initialized";
             try {
-                dispatchState(ctx, buffer, channel);
+                dispatchState(buffer, channel);
             } catch (Throwable t) {
                 ignoreTillSync = true;
                 try {
@@ -313,21 +305,18 @@ public class PostgresWireProtocol {
                 } catch (Throwable ti) {
                     LOGGER.error("Error trying to send error to client: {}", t, ti);
                 }
-                ctx.read();
             }
         }
 
-        private void dispatchState(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchState(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.state()) {
                 case STARTUP_PARAMETERS:
                     handleStartupBody(buffer, channel);
                     decoder.startupDone();
-                    ctx.read();
                     return;
 
                 case CANCEL:
                     handleCancelRequestBody(buffer, channel);
-                    ctx.read();
                     return;
 
                 case MSG:
@@ -335,55 +324,47 @@ public class PostgresWireProtocol {
 
                     if (ignoreTillSync && decoder.msgType() != 'S') {
                         buffer.skipBytes(decoder.payloadLength());
-                        ctx.read();
                         return;
                     }
-                    dispatchMessage(ctx, buffer, channel);
+                    dispatchMessage(buffer, channel);
                     return;
                 default:
                     throw new IllegalStateException("Illegal state: " + decoder.state());
             }
         }
 
-        private void dispatchMessage(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchMessage(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.msgType()) {
                 case 'Q': // Query (simple)
-                    handleSimpleQuery(ctx::read, buffer, channel);
+                    handleSimpleQuery(buffer, channel);
                     return;
                 case 'P':
                     handleParseMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'p':
                     handlePassword(buffer, channel);
-                    ctx.read();
                     return;
                 case 'B':
                     handleBindMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'D':
                     handleDescribeMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'E':
-                    handleExecute(ctx, buffer, channel);
+                    handleExecute(buffer, channel);
                     return;
                 case 'H':
                     handleFlush(channel);
-                    ctx.read();
                     return;
                 case 'S':
-                    handleSync(ctx, channel);
+                    handleSync(channel);
                     return;
                 case 'C':
                     handleClose(buffer, channel);
-                    ctx.read();
                     return;
                 case 'X': // Terminate (called when jdbc connection is closed)
                     closeSession();
                     channel.close();
-                    ctx.read();
                     return;
                 default:
                     Messages.sendErrorResponse(
@@ -392,7 +373,6 @@ public class PostgresWireProtocol {
                             ? AccessControl.DISABLED
                             : getAccessControl.apply(session.sessionSettings()),
                         new UnsupportedOperationException("Unsupported messageType: " + decoder.msgType()));
-                    ctx.read();
             }
         }
 
@@ -479,9 +459,9 @@ public class PostgresWireProtocol {
                 applyOptions(options);
             }
             Messages.sendAuthenticationOK(channel)
-                .addListener(_ -> sendParams(channel, session.sessionSettings()))
-                .addListener(_ -> Messages.sendKeyData(channel, session.id(), session.secret()))
-                .addListener(_ -> {
+                .addListener(f -> sendParams(channel, session.sessionSettings()))
+                .addListener(f -> Messages.sendKeyData(channel, session.id(), session.secret()))
+                .addListener(f -> {
                     sendReadyForQuery(channel, TransactionState.IDLE);
                     if (properties.containsKey("CrateDBTransport")) {
                         switchToTransportProtocol(channel);
@@ -704,7 +684,7 @@ public class PostgresWireProtocol {
      * | string portalName
      * | int32 maxRows (0 = unlimited)
      */
-    private void handleExecute(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+    private void handleExecute(ByteBuf buffer, DelayableWriteChannel channel) {
         String portalName = readCString(buffer);
         int maxRows = buffer.readInt();
         String query = session.getQuery(portalName);
@@ -715,6 +695,25 @@ public class PostgresWireProtocol {
             return;
         }
         List<? extends DataType<?>> outputTypes = session.getOutputTypes(portalName);
+
+        // .execute is going async and may execute the query in another thread-pool.
+        // The results are later sent to the clients via the `ResultReceiver` created
+        // above, The `channel.write` calls - which the `ResultReceiver` makes - may
+        // happen in a thread which is *not* a netty thread.
+        // If that is the case, netty schedules the writes instead of running them
+        // immediately. A consequence of that is that *this* thread can continue
+        // processing other messages from the client, and if this thread then sends messages to the
+        // client, these are sent immediately, overtaking the result messages of the
+        // execute that is triggered here.
+        //
+        // This would lead to out-of-order messages. For example, we could send a
+        // `parseComplete` before the `commandComplete` of the previous statement has
+        // been transmitted.
+        //
+        // To ensure clients receive messages in the correct order we delay all writes
+        // The "finish" logic of the ResultReceivers writes out all pending writes/unblocks the channel
+
+        DelayedWrites delayedWrites = channel.delayWrites();
         ResultReceiver<?> resultReceiver;
         if (outputTypes == null) {
             // this is a DML query
@@ -722,6 +721,7 @@ public class PostgresWireProtocol {
             resultReceiver = new RowCountReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings())
             );
         } else {
@@ -729,21 +729,16 @@ public class PostgresWireProtocol {
             resultReceiver = new ResultSetReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings()),
                 Lists.map(outputTypes, PGTypes::get),
                 session.getResultFormatCodes(portalName)
             );
         }
-        @Nullable
-        CompletableFuture<?> pendingExecution = session.execute(portalName, maxRows, resultReceiver);
-        if (pendingExecution == null) {
-            ctx.read();
-        } else {
-            pendingExecution.whenComplete((_, _) -> ctx.read());
-        }
+        session.execute(portalName, maxRows, resultReceiver);
     }
 
-    private void handleSync(ChannelHandlerContext ctx, Channel channel) {
+    private void handleSync(DelayableWriteChannel channel) {
         if (ignoreTillSync) {
             ignoreTillSync = false;
             // If an error happens all sub-sequent messages can be ignored until the client sends a sync message
@@ -756,17 +751,17 @@ public class PostgresWireProtocol {
             //  4) p, b, e    -> We've a new query deferred.
             //  5) `sync`     -> We must execute the query from 4, but not 1)
             session.resetDeferredExecutions();
+            channel.writePendingMessages();
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
             return;
         }
         try {
-            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(ctx::read, channel, session.transactionState());
+            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(channel, session.transactionState());
             session.sync(false).whenComplete(readyForQueryCallback);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), t);
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
         }
     }
 
@@ -781,7 +776,7 @@ public class PostgresWireProtocol {
     }
 
     @VisibleForTesting
-    void handleSimpleQuery(Runnable read, ByteBuf buffer, final Channel channel) {
+    void handleSimpleQuery(ByteBuf buffer, final DelayableWriteChannel channel) {
         assert session != null : "Session must be created when running a simple query";
         Session.TimeoutToken timeoutToken = session.newTimeoutToken();
         String queryString = readCString(buffer);
@@ -799,7 +794,6 @@ public class PostgresWireProtocol {
         } catch (Exception ex) {
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), ex);
             sendReadyForQuery(channel, TransactionState.IDLE);
-            read.run();
             return;
         }
         timeoutToken.check();
@@ -807,12 +801,12 @@ public class PostgresWireProtocol {
         for (var statement : statements) {
             composedFuture = composedFuture.thenCompose(result -> handleSingleQuery(statement, queryString, channel, timeoutToken));
         }
-        composedFuture.whenComplete(new ReadyForQueryCallback(read, channel, TransactionState.IDLE));
+        composedFuture.whenComplete(new ReadyForQueryCallback(channel, TransactionState.IDLE));
     }
 
     private CompletableFuture<?> handleSingleQuery(Statement statement,
                                                    String query,
-                                                   Channel channel,
+                                                   DelayableWriteChannel channel,
                                                    Session.TimeoutToken timeoutToken) {
         CompletableFuture<?> result = new CompletableFuture<>();
 
@@ -831,17 +825,21 @@ public class PostgresWireProtocol {
             List<Symbol> fields = describeResult.getFields();
 
             if (fields == null) {
+                DelayedWrites delayedWrites = channel.delayWrites();
                 RowCountReceiver rowCountReceiver = new RowCountReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl
                 );
                 session.execute("", 0, rowCountReceiver);
             } else {
                 Messages.sendRowDescription(channel, fields, null, describeResult.relation());
+                DelayedWrites delayedWrites = channel.delayWrites();
                 ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl,
                     Lists.map(fields, x -> PGTypes.get(x.valueType())),
                     null
@@ -850,6 +848,7 @@ public class PostgresWireProtocol {
             }
             return session.sync(false);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, accessControl, t);
             result.completeExceptionally(t);
             return result;
diff --git a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
index d7a09fa191..9c6f657a6c 100644
--- a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
@@ -29,6 +29,7 @@ import org.jetbrains.annotations.Nullable;
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.session.BaseResultReceiver;
 import io.netty.channel.Channel;
@@ -37,9 +38,11 @@ import io.netty.channel.ChannelFuture;
 class ResultSetReceiver extends BaseResultReceiver {
 
     private final String query;
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final List<PGType<?>> columnTypes;
     private final AccessControl accessControl;
+    private final Channel directChannel;
+    private final DelayedWrites delayedWrites;
 
     @Nullable
     private final FormatCodes.FormatCode[] formatCodes;
@@ -47,12 +50,15 @@ class ResultSetReceiver extends BaseResultReceiver {
     private long rowCount = 0;
 
     ResultSetReceiver(String query,
-                      Channel channel,
+                      DelayableWriteChannel channel,
+                      DelayedWrites delayedWrites,
                       AccessControl accessControl,
                       List<PGType<?>> columnTypes,
                       @Nullable FormatCodes.FormatCode[] formatCodes) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
+        this.directChannel = channel.bypassDelay();
         this.accessControl = accessControl;
         this.columnTypes = columnTypes;
         this.formatCodes = formatCodes;
@@ -67,9 +73,9 @@ class ResultSetReceiver extends BaseResultReceiver {
     @Nullable
     public CompletableFuture<Void> setNextRow(Row row) {
         rowCount++;
-        ChannelFuture sendDataRow = Messages.sendDataRow(channel, row, columnTypes, formatCodes);
+        ChannelFuture sendDataRow = Messages.sendDataRow(directChannel, row, columnTypes, formatCodes);
         CompletableFuture<Void> future;
-        boolean isWritable = channel.isWritable();
+        boolean isWritable = directChannel.isWritable();
         if (isWritable) {
             future = null;
         } else {
@@ -89,33 +95,36 @@ class ResultSetReceiver extends BaseResultReceiver {
         // Flush the channel only every 1000 rows for better performance.
         // But flushing must be forced once the channel outbound buffer is full (= channel not in writable state)
         if (isWritable == false || rowCount % 1000 == 0) {
-            channel.flush();
+            directChannel.flush();
         }
         return future;
     }
 
     @Override
     public void batchFinished() {
-        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(channel);
+        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(directChannel);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
 
         // Trigger the completion future but by-pass `sendCompleteComplete`
         // This resultReceiver shouldn't be used anymore. The next `execute` message
         // from the client will create a new one.
-        sendPortalSuspended.addListener(_ -> super.allFinished());
+        sendPortalSuspended.addListener(f -> super.allFinished());
     }
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(directChannel, query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(directChannel, accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
index d752160edd..7ef1bdc276 100644
--- a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
@@ -26,24 +26,27 @@ import java.util.concurrent.CompletableFuture;
 import org.jetbrains.annotations.NotNull;
 import org.jetbrains.annotations.Nullable;
 
+import io.crate.session.BaseResultReceiver;
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
-import io.crate.session.BaseResultReceiver;
-import io.netty.channel.Channel;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.netty.channel.ChannelFuture;
 
 class RowCountReceiver extends BaseResultReceiver {
 
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final String query;
     private final AccessControl accessControl;
+    private final DelayedWrites delayedWrites;
     private long rowCount;
 
     RowCountReceiver(String query,
-                     Channel channel,
+                     DelayableWriteChannel channel,
+                     DelayedWrites delayedWrites,
                      AccessControl accessControl) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
         this.accessControl = accessControl;
     }
 
@@ -63,15 +66,17 @@ class RowCountReceiver extends BaseResultReceiver {
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel.bypassDelay(), query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel.bypassDelay(), accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
index 9dbb95487f..77cca1144d 100644
--- a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
+++ b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
@@ -277,8 +277,7 @@ public class Netty4Transport extends TcpTransport {
             maybeInjectSSL(ch);
             ch.pipeline().addLast("logging", loggingHandler);
             // using a dot as a prefix means this cannot come from any settings parsed
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override
@@ -320,8 +319,7 @@ public class Netty4Transport extends TcpTransport {
             ch.attr(CHANNEL_KEY).set(nettyTcpChannel);
             serverAcceptedChannel(nettyTcpChannel);
             ch.pipeline().addLast("logging", loggingHandler);
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override

```
## Full Developer Backport Patch (full commit diff)
```diff
diff --git a/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
new file mode 100644
index 0000000000..d7fd559f2c
--- /dev/null
+++ b/server/src/main/java/io/crate/protocols/postgres/DelayableWriteChannel.java
@@ -0,0 +1,355 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import java.net.SocketAddress;
+import java.util.ArrayDeque;
+
+import org.jetbrains.annotations.Nullable;
+
+import io.netty.buffer.ByteBufAllocator;
+import io.netty.channel.Channel;
+import io.netty.channel.ChannelConfig;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelId;
+import io.netty.channel.ChannelMetadata;
+import io.netty.channel.ChannelPipeline;
+import io.netty.channel.ChannelProgressivePromise;
+import io.netty.channel.ChannelPromise;
+import io.netty.channel.EventLoop;
+import io.netty.util.Attribute;
+import io.netty.util.AttributeKey;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * Channel implementation that allows to delay writes with `blockWritesUntil`
+ **/
+public class DelayableWriteChannel implements Channel {
+
+    private final Channel delegate;
+    private DelayedWrites delay = null;
+
+    public DelayableWriteChannel(Channel channel) {
+        this.delegate = channel;
+        channel.closeFuture().addListener(_ -> discardDelayedWrites());
+    }
+
+    @Override
+    public <T> Attribute<T> attr(AttributeKey<T> key) {
+        return delegate.attr(key);
+    }
+
+    @Override
+    public <T> boolean hasAttr(AttributeKey<T> key) {
+        return delegate.hasAttr(key);
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress) {
+        return delegate.bind(localAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress) {
+        return delegate.connect(remoteAddress);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress) {
+        return delegate.connect(remoteAddress, localAddress);
+    }
+
+    @Override
+    public ChannelFuture disconnect() {
+        return delegate.disconnect();
+    }
+
+    @Override
+    public ChannelFuture close() {
+        return delegate.close();
+    }
+
+    @Override
+    public ChannelFuture deregister() {
+        return delegate.deregister();
+    }
+
+    @Override
+    public ChannelFuture bind(SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.bind(localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture connect(SocketAddress remoteAddress, SocketAddress localAddress, ChannelPromise promise) {
+        return delegate.connect(remoteAddress, localAddress, promise);
+    }
+
+    @Override
+    public ChannelFuture disconnect(ChannelPromise promise) {
+        return delegate.disconnect(promise);
+    }
+
+    @Override
+    public ChannelFuture close(ChannelPromise promise) {
+        return delegate.close(promise);
+    }
+
+    @Override
+    public ChannelFuture deregister(ChannelPromise promise) {
+        return delegate.deregister(promise);
+    }
+
+    @Override
+    public ChannelFuture write(Object msg) {
+        return this.write(msg, newPromise());
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg) {
+        return this.writeAndFlush(msg, newPromise());
+    }
+
+    @Override
+    public ChannelPromise newPromise() {
+        return delegate.newPromise();
+    }
+
+    @Override
+    public ChannelProgressivePromise newProgressivePromise() {
+        return delegate.newProgressivePromise();
+    }
+
+    @Override
+    public ChannelFuture newSucceededFuture() {
+        return delegate.newSucceededFuture();
+    }
+
+    @Override
+    public ChannelFuture newFailedFuture(Throwable cause) {
+        return delegate.newFailedFuture(cause);
+    }
+
+    @Override
+    public ChannelPromise voidPromise() {
+        return delegate.voidPromise();
+    }
+
+    @Override
+    public int compareTo(Channel o) {
+        return delegate.compareTo(o);
+    }
+
+    @Override
+    public ChannelId id() {
+        return delegate.id();
+    }
+
+    @Override
+    public EventLoop eventLoop() {
+        return delegate.eventLoop();
+    }
+
+    @Override
+    public Channel parent() {
+        return delegate.parent();
+    }
+
+    @Override
+    public ChannelConfig config() {
+        return delegate.config();
+    }
+
+    @Override
+    public boolean isOpen() {
+        return delegate.isOpen();
+    }
+
+    @Override
+    public boolean isRegistered() {
+        return delegate.isRegistered();
+    }
+
+    @Override
+    public boolean isActive() {
+        return delegate.isActive();
+    }
+
+    @Override
+    public ChannelMetadata metadata() {
+        return delegate.metadata();
+    }
+
+    @Override
+    public SocketAddress localAddress() {
+        return delegate.localAddress();
+    }
+
+    @Override
+    public SocketAddress remoteAddress() {
+        return delegate.remoteAddress();
+    }
+
+    @Override
+    public ChannelFuture closeFuture() {
+        return delegate.closeFuture();
+    }
+
+    @Override
+    public boolean isWritable() {
+        return delegate.isWritable();
+    }
+
+    @Override
+    public long bytesBeforeUnwritable() {
+        return delegate.bytesBeforeUnwritable();
+    }
+
+    @Override
+    public long bytesBeforeWritable() {
+        return delegate.bytesBeforeWritable();
+    }
+
+    @Override
+    public Unsafe unsafe() {
+        return delegate.unsafe();
+    }
+
+    @Override
+    public ChannelPipeline pipeline() {
+        return delegate.pipeline();
+    }
+
+    @Override
+    public ByteBufAllocator alloc() {
+        return delegate.alloc();
+    }
+
+    @Override
+    public Channel read() {
+        return delegate.read();
+    }
+
+    @Override
+    public Channel flush() {
+        return delegate.flush();
+    }
+
+    public Channel bypassDelay() {
+        return delegate;
+    }
+
+
+    @Override
+    public ChannelFuture write(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.write(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.write(msg, promise);
+    }
+
+    @Override
+    public ChannelFuture writeAndFlush(Object msg, ChannelPromise promise) {
+        synchronized (this) {
+            if (delay != null) {
+                delay.add(msg, () -> delegate.writeAndFlush(msg, promise));
+                return promise;
+            }
+        }
+        return delegate.writeAndFlush(msg, promise);
+    }
+
+    public synchronized void discardDelayedWrites() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.discard();
+                parent = parent.parent;
+            }
+            delay.discard();
+            delay = null;
+        }
+    }
+
+    public synchronized void writePendingMessages(DelayedWrites delayedWrites) {
+        if (delay == delayedWrites) {
+            delay = null;
+        }
+        delayedWrites.writeDelayed();
+    }
+
+    public synchronized void writePendingMessages() {
+        if (delay != null) {
+            var parent = delay.parent;
+            while (parent != null) {
+                parent.writeDelayed();
+                parent = parent.parent;
+            }
+            delay.writeDelayed();
+            delay = null;
+        }
+    }
+
+    public DelayedWrites delayWrites() {
+        DelayedWrites delayedWrites = new DelayedWrites(delay);
+        delay = delayedWrites;
+        return delayedWrites;
+    }
+
+    record DelayedMsg(Object msg, Runnable runnable) {
+    }
+
+    static class DelayedWrites {
+
+        private final ArrayDeque<DelayedMsg> delayed = new ArrayDeque<>();
+        private final DelayedWrites parent;
+
+        public DelayedWrites(@Nullable DelayedWrites parent) {
+            this.parent = parent;
+        }
+
+        public void discard() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                ReferenceCountUtil.safeRelease(delayedMsg.msg);
+            }
+        }
+
+        public void add(Object msg, Runnable runnable) {
+            delayed.add(new DelayedMsg(msg, runnable));
+        }
+
+        private void writeDelayed() {
+            DelayedMsg delayedMsg;
+            while ((delayedMsg = delayed.poll()) != null) {
+                delayedMsg.runnable.run();
+            }
+        }
+    }
+}
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
index b596538315..30199e1288 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresNetty.java
@@ -70,7 +70,6 @@ import io.crate.types.DataTypes;
 import io.netty.bootstrap.ServerBootstrap;
 import io.netty.channel.Channel;
 import io.netty.channel.ChannelInitializer;
-import io.netty.channel.ChannelOption;
 import io.netty.channel.ChannelPipeline;
 import io.netty.handler.ssl.SslContext;
 
@@ -168,7 +167,6 @@ public class PostgresNetty extends AbstractLifecycleComponent {
         }
         var eventLoopGroup = nettyBootstrap.getSharedEventLoopGroup();
         bootstrap = NettyBootstrap.newServerBootstrap(settings, eventLoopGroup);
-        bootstrap.childOption(ChannelOption.AUTO_READ, false);
         inboundStatsHandler = new Netty4InboundStatsHandler(statsTracker, LOGGER);
         outboundStatsHandler = new Netty4OutboundStatsHandler(statsTracker, LOGGER);
 
@@ -189,8 +187,7 @@ public class PostgresNetty extends AbstractLifecycleComponent {
                     chPipeline -> {
                         var nettyTcpChannel = new CloseableChannel(ch, true);
                         ch.attr(Netty4Transport.CHANNEL_KEY).set(nettyTcpChannel);
-                        var handler = new Netty4MessageChannelHandler(pageCacheRecycler, transport, false);
-                        chPipeline.addLast("dispatcher", handler);
+                        chPipeline.addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, transport));
                     },
                     authentication,
                     sslContextProvider
diff --git a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
index e016fbc588..9f7aff8974 100644
--- a/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
+++ b/server/src/main/java/io/crate/protocols/postgres/PostgresWireProtocol.java
@@ -61,6 +61,7 @@ import io.crate.expression.symbol.Symbol;
 import io.crate.metadata.settings.CoordinatorSessionSettings;
 import io.crate.metadata.settings.session.SessionSetting;
 import io.crate.metadata.settings.session.SessionSettingRegistry;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.role.Role;
@@ -205,7 +206,7 @@ public class PostgresWireProtocol {
     private final Authentication authService;
     private final Consumer<ChannelPipeline> addTransportHandler;
 
-    private Channel channel;
+    private DelayableWriteChannel channel;
     Session session;
     private boolean ignoreTillSync = false;
     private AuthenticationContext authContext;
@@ -265,10 +266,8 @@ public class PostgresWireProtocol {
     private static class ReadyForQueryCallback implements BiConsumer<Object, Throwable> {
         private final Channel channel;
         private final TransactionState transactionState;
-        private final Runnable read;
 
-        private ReadyForQueryCallback(Runnable read, Channel channel, TransactionState transactionState) {
-            this.read = read;
+        private ReadyForQueryCallback(Channel channel, TransactionState transactionState) {
             this.channel = channel;
             this.transactionState = transactionState;
         }
@@ -276,7 +275,6 @@ public class PostgresWireProtocol {
         @Override
         public void accept(Object result, Throwable t) {
             sendReadyForQuery(channel, transactionState);
-            read.run();
         }
     }
 
@@ -284,7 +282,7 @@ public class PostgresWireProtocol {
 
         @Override
         public void channelRegistered(ChannelHandlerContext ctx) throws Exception {
-            channel = ctx.channel();
+            channel = new DelayableWriteChannel(ctx.channel());
         }
 
         @Override
@@ -292,17 +290,11 @@ public class PostgresWireProtocol {
             return true;
         }
 
-        @Override
-        public void channelActive(ChannelHandlerContext ctx) throws Exception {
-            super.channelActive(ctx);
-            ctx.read();
-        }
-
         @Override
         public void channelRead0(ChannelHandlerContext ctx, ByteBuf buffer) throws Exception {
             assert channel != null : "Channel must be initialized";
             try {
-                dispatchState(ctx, buffer, channel);
+                dispatchState(buffer, channel);
             } catch (Throwable t) {
                 ignoreTillSync = true;
                 try {
@@ -313,21 +305,18 @@ public class PostgresWireProtocol {
                 } catch (Throwable ti) {
                     LOGGER.error("Error trying to send error to client: {}", t, ti);
                 }
-                ctx.read();
             }
         }
 
-        private void dispatchState(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchState(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.state()) {
                 case STARTUP_PARAMETERS:
                     handleStartupBody(buffer, channel);
                     decoder.startupDone();
-                    ctx.read();
                     return;
 
                 case CANCEL:
                     handleCancelRequestBody(buffer, channel);
-                    ctx.read();
                     return;
 
                 case MSG:
@@ -335,55 +324,47 @@ public class PostgresWireProtocol {
 
                     if (ignoreTillSync && decoder.msgType() != 'S') {
                         buffer.skipBytes(decoder.payloadLength());
-                        ctx.read();
                         return;
                     }
-                    dispatchMessage(ctx, buffer, channel);
+                    dispatchMessage(buffer, channel);
                     return;
                 default:
                     throw new IllegalStateException("Illegal state: " + decoder.state());
             }
         }
 
-        private void dispatchMessage(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+        private void dispatchMessage(ByteBuf buffer, DelayableWriteChannel channel) {
             switch (decoder.msgType()) {
                 case 'Q': // Query (simple)
-                    handleSimpleQuery(ctx::read, buffer, channel);
+                    handleSimpleQuery(buffer, channel);
                     return;
                 case 'P':
                     handleParseMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'p':
                     handlePassword(buffer, channel);
-                    ctx.read();
                     return;
                 case 'B':
                     handleBindMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'D':
                     handleDescribeMessage(buffer, channel);
-                    ctx.read();
                     return;
                 case 'E':
-                    handleExecute(ctx, buffer, channel);
+                    handleExecute(buffer, channel);
                     return;
                 case 'H':
                     handleFlush(channel);
-                    ctx.read();
                     return;
                 case 'S':
-                    handleSync(ctx, channel);
+                    handleSync(channel);
                     return;
                 case 'C':
                     handleClose(buffer, channel);
-                    ctx.read();
                     return;
                 case 'X': // Terminate (called when jdbc connection is closed)
                     closeSession();
                     channel.close();
-                    ctx.read();
                     return;
                 default:
                     Messages.sendErrorResponse(
@@ -392,7 +373,6 @@ public class PostgresWireProtocol {
                             ? AccessControl.DISABLED
                             : getAccessControl.apply(session.sessionSettings()),
                         new UnsupportedOperationException("Unsupported messageType: " + decoder.msgType()));
-                    ctx.read();
             }
         }
 
@@ -479,9 +459,9 @@ public class PostgresWireProtocol {
                 applyOptions(options);
             }
             Messages.sendAuthenticationOK(channel)
-                .addListener(_ -> sendParams(channel, session.sessionSettings()))
-                .addListener(_ -> Messages.sendKeyData(channel, session.id(), session.secret()))
-                .addListener(_ -> {
+                .addListener(f -> sendParams(channel, session.sessionSettings()))
+                .addListener(f -> Messages.sendKeyData(channel, session.id(), session.secret()))
+                .addListener(f -> {
                     sendReadyForQuery(channel, TransactionState.IDLE);
                     if (properties.containsKey("CrateDBTransport")) {
                         switchToTransportProtocol(channel);
@@ -704,7 +684,7 @@ public class PostgresWireProtocol {
      * | string portalName
      * | int32 maxRows (0 = unlimited)
      */
-    private void handleExecute(ChannelHandlerContext ctx, ByteBuf buffer, Channel channel) {
+    private void handleExecute(ByteBuf buffer, DelayableWriteChannel channel) {
         String portalName = readCString(buffer);
         int maxRows = buffer.readInt();
         String query = session.getQuery(portalName);
@@ -715,6 +695,25 @@ public class PostgresWireProtocol {
             return;
         }
         List<? extends DataType<?>> outputTypes = session.getOutputTypes(portalName);
+
+        // .execute is going async and may execute the query in another thread-pool.
+        // The results are later sent to the clients via the `ResultReceiver` created
+        // above, The `channel.write` calls - which the `ResultReceiver` makes - may
+        // happen in a thread which is *not* a netty thread.
+        // If that is the case, netty schedules the writes instead of running them
+        // immediately. A consequence of that is that *this* thread can continue
+        // processing other messages from the client, and if this thread then sends messages to the
+        // client, these are sent immediately, overtaking the result messages of the
+        // execute that is triggered here.
+        //
+        // This would lead to out-of-order messages. For example, we could send a
+        // `parseComplete` before the `commandComplete` of the previous statement has
+        // been transmitted.
+        //
+        // To ensure clients receive messages in the correct order we delay all writes
+        // The "finish" logic of the ResultReceivers writes out all pending writes/unblocks the channel
+
+        DelayedWrites delayedWrites = channel.delayWrites();
         ResultReceiver<?> resultReceiver;
         if (outputTypes == null) {
             // this is a DML query
@@ -722,6 +721,7 @@ public class PostgresWireProtocol {
             resultReceiver = new RowCountReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings())
             );
         } else {
@@ -729,21 +729,16 @@ public class PostgresWireProtocol {
             resultReceiver = new ResultSetReceiver(
                 query,
                 channel,
+                delayedWrites,
                 getAccessControl.apply(session.sessionSettings()),
                 Lists.map(outputTypes, PGTypes::get),
                 session.getResultFormatCodes(portalName)
             );
         }
-        @Nullable
-        CompletableFuture<?> pendingExecution = session.execute(portalName, maxRows, resultReceiver);
-        if (pendingExecution == null) {
-            ctx.read();
-        } else {
-            pendingExecution.whenComplete((_, _) -> ctx.read());
-        }
+        session.execute(portalName, maxRows, resultReceiver);
     }
 
-    private void handleSync(ChannelHandlerContext ctx, Channel channel) {
+    private void handleSync(DelayableWriteChannel channel) {
         if (ignoreTillSync) {
             ignoreTillSync = false;
             // If an error happens all sub-sequent messages can be ignored until the client sends a sync message
@@ -756,17 +751,17 @@ public class PostgresWireProtocol {
             //  4) p, b, e    -> We've a new query deferred.
             //  5) `sync`     -> We must execute the query from 4, but not 1)
             session.resetDeferredExecutions();
+            channel.writePendingMessages();
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
             return;
         }
         try {
-            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(ctx::read, channel, session.transactionState());
+            ReadyForQueryCallback readyForQueryCallback = new ReadyForQueryCallback(channel, session.transactionState());
             session.sync(false).whenComplete(readyForQueryCallback);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), t);
             sendReadyForQuery(channel, TransactionState.FAILED_TRANSACTION);
-            ctx.read();
         }
     }
 
@@ -781,7 +776,7 @@ public class PostgresWireProtocol {
     }
 
     @VisibleForTesting
-    void handleSimpleQuery(Runnable read, ByteBuf buffer, final Channel channel) {
+    void handleSimpleQuery(ByteBuf buffer, final DelayableWriteChannel channel) {
         assert session != null : "Session must be created when running a simple query";
         Session.TimeoutToken timeoutToken = session.newTimeoutToken();
         String queryString = readCString(buffer);
@@ -799,7 +794,6 @@ public class PostgresWireProtocol {
         } catch (Exception ex) {
             Messages.sendErrorResponse(channel, getAccessControl.apply(session.sessionSettings()), ex);
             sendReadyForQuery(channel, TransactionState.IDLE);
-            read.run();
             return;
         }
         timeoutToken.check();
@@ -807,12 +801,12 @@ public class PostgresWireProtocol {
         for (var statement : statements) {
             composedFuture = composedFuture.thenCompose(result -> handleSingleQuery(statement, queryString, channel, timeoutToken));
         }
-        composedFuture.whenComplete(new ReadyForQueryCallback(read, channel, TransactionState.IDLE));
+        composedFuture.whenComplete(new ReadyForQueryCallback(channel, TransactionState.IDLE));
     }
 
     private CompletableFuture<?> handleSingleQuery(Statement statement,
                                                    String query,
-                                                   Channel channel,
+                                                   DelayableWriteChannel channel,
                                                    Session.TimeoutToken timeoutToken) {
         CompletableFuture<?> result = new CompletableFuture<>();
 
@@ -831,17 +825,21 @@ public class PostgresWireProtocol {
             List<Symbol> fields = describeResult.getFields();
 
             if (fields == null) {
+                DelayedWrites delayedWrites = channel.delayWrites();
                 RowCountReceiver rowCountReceiver = new RowCountReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl
                 );
                 session.execute("", 0, rowCountReceiver);
             } else {
                 Messages.sendRowDescription(channel, fields, null, describeResult.relation());
+                DelayedWrites delayedWrites = channel.delayWrites();
                 ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
                     query,
                     channel,
+                    delayedWrites,
                     accessControl,
                     Lists.map(fields, x -> PGTypes.get(x.valueType())),
                     null
@@ -850,6 +848,7 @@ public class PostgresWireProtocol {
             }
             return session.sync(false);
         } catch (Throwable t) {
+            channel.discardDelayedWrites();
             Messages.sendErrorResponse(channel, accessControl, t);
             result.completeExceptionally(t);
             return result;
diff --git a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
index d7a09fa191..9c6f657a6c 100644
--- a/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/ResultSetReceiver.java
@@ -29,6 +29,7 @@ import org.jetbrains.annotations.Nullable;
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGType;
 import io.crate.session.BaseResultReceiver;
 import io.netty.channel.Channel;
@@ -37,9 +38,11 @@ import io.netty.channel.ChannelFuture;
 class ResultSetReceiver extends BaseResultReceiver {
 
     private final String query;
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final List<PGType<?>> columnTypes;
     private final AccessControl accessControl;
+    private final Channel directChannel;
+    private final DelayedWrites delayedWrites;
 
     @Nullable
     private final FormatCodes.FormatCode[] formatCodes;
@@ -47,12 +50,15 @@ class ResultSetReceiver extends BaseResultReceiver {
     private long rowCount = 0;
 
     ResultSetReceiver(String query,
-                      Channel channel,
+                      DelayableWriteChannel channel,
+                      DelayedWrites delayedWrites,
                       AccessControl accessControl,
                       List<PGType<?>> columnTypes,
                       @Nullable FormatCodes.FormatCode[] formatCodes) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
+        this.directChannel = channel.bypassDelay();
         this.accessControl = accessControl;
         this.columnTypes = columnTypes;
         this.formatCodes = formatCodes;
@@ -67,9 +73,9 @@ class ResultSetReceiver extends BaseResultReceiver {
     @Nullable
     public CompletableFuture<Void> setNextRow(Row row) {
         rowCount++;
-        ChannelFuture sendDataRow = Messages.sendDataRow(channel, row, columnTypes, formatCodes);
+        ChannelFuture sendDataRow = Messages.sendDataRow(directChannel, row, columnTypes, formatCodes);
         CompletableFuture<Void> future;
-        boolean isWritable = channel.isWritable();
+        boolean isWritable = directChannel.isWritable();
         if (isWritable) {
             future = null;
         } else {
@@ -89,33 +95,36 @@ class ResultSetReceiver extends BaseResultReceiver {
         // Flush the channel only every 1000 rows for better performance.
         // But flushing must be forced once the channel outbound buffer is full (= channel not in writable state)
         if (isWritable == false || rowCount % 1000 == 0) {
-            channel.flush();
+            directChannel.flush();
         }
         return future;
     }
 
     @Override
     public void batchFinished() {
-        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(channel);
+        ChannelFuture sendPortalSuspended = Messages.sendPortalSuspended(directChannel);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
 
         // Trigger the completion future but by-pass `sendCompleteComplete`
         // This resultReceiver shouldn't be used anymore. The next `execute` message
         // from the client will create a new one.
-        sendPortalSuspended.addListener(_ -> super.allFinished());
+        sendPortalSuspended.addListener(f -> super.allFinished());
     }
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(directChannel, query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(directChannel, accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
index d752160edd..7ef1bdc276 100644
--- a/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
+++ b/server/src/main/java/io/crate/protocols/postgres/RowCountReceiver.java
@@ -26,24 +26,27 @@ import java.util.concurrent.CompletableFuture;
 import org.jetbrains.annotations.NotNull;
 import org.jetbrains.annotations.Nullable;
 
+import io.crate.session.BaseResultReceiver;
 import io.crate.auth.AccessControl;
 import io.crate.data.Row;
-import io.crate.session.BaseResultReceiver;
-import io.netty.channel.Channel;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.netty.channel.ChannelFuture;
 
 class RowCountReceiver extends BaseResultReceiver {
 
-    private final Channel channel;
+    private final DelayableWriteChannel channel;
     private final String query;
     private final AccessControl accessControl;
+    private final DelayedWrites delayedWrites;
     private long rowCount;
 
     RowCountReceiver(String query,
-                     Channel channel,
+                     DelayableWriteChannel channel,
+                     DelayedWrites delayedWrites,
                      AccessControl accessControl) {
         this.query = query;
         this.channel = channel;
+        this.delayedWrites = delayedWrites;
         this.accessControl = accessControl;
     }
 
@@ -63,15 +66,17 @@ class RowCountReceiver extends BaseResultReceiver {
 
     @Override
     public void allFinished() {
-        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel, query, rowCount);
+        ChannelFuture sendCommandComplete = Messages.sendCommandComplete(channel.bypassDelay(), query, rowCount);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendCommandComplete.addListener(_ -> super.allFinished());
+        sendCommandComplete.addListener(f -> super.allFinished());
     }
 
     @Override
     public void fail(@NotNull Throwable throwable) {
-        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel, accessControl, throwable);
+        ChannelFuture sendErrorResponse = Messages.sendErrorResponse(channel.bypassDelay(), accessControl, throwable);
+        channel.writePendingMessages(delayedWrites);
         channel.flush();
-        sendErrorResponse.addListener(_ -> super.fail(throwable));
+        sendErrorResponse.addListener(f -> super.fail(throwable));
     }
 }
diff --git a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
index 9dbb95487f..77cca1144d 100644
--- a/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
+++ b/server/src/main/java/org/elasticsearch/transport/netty4/Netty4Transport.java
@@ -277,8 +277,7 @@ public class Netty4Transport extends TcpTransport {
             maybeInjectSSL(ch);
             ch.pipeline().addLast("logging", loggingHandler);
             // using a dot as a prefix means this cannot come from any settings parsed
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override
@@ -320,8 +319,7 @@ public class Netty4Transport extends TcpTransport {
             ch.attr(CHANNEL_KEY).set(nettyTcpChannel);
             serverAcceptedChannel(nettyTcpChannel);
             ch.pipeline().addLast("logging", loggingHandler);
-            var handler = new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this);
-            ch.pipeline().addLast("dispatcher", handler);
+            ch.pipeline().addLast("dispatcher", new Netty4MessageChannelHandler(pageCacheRecycler, Netty4Transport.this));
         }
 
         @Override
diff --git a/server/src/test/java/io/crate/protocols/postgres/DelayableWriteChannelTest.java b/server/src/test/java/io/crate/protocols/postgres/DelayableWriteChannelTest.java
new file mode 100644
index 0000000000..4515a9d614
--- /dev/null
+++ b/server/src/test/java/io/crate/protocols/postgres/DelayableWriteChannelTest.java
@@ -0,0 +1,80 @@
+/*
+ * Licensed to Crate.io GmbH ("Crate") under one or more contributor
+ * license agreements.  See the NOTICE file distributed with this work for
+ * additional information regarding copyright ownership.  Crate licenses
+ * this file to you under the Apache License, Version 2.0 (the "License");
+ * you may not use this file except in compliance with the License.  You may
+ * obtain a copy of the License at
+ *
+ *   http://www.apache.org/licenses/LICENSE-2.0
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
+ * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
+ * License for the specific language governing permissions and limitations
+ * under the License.
+ *
+ * However, if you have executed another commercial license agreement
+ * with Crate these terms will supersede the license and you may use the
+ * software solely pursuant to the terms of the relevant commercial agreement.
+ */
+
+package io.crate.protocols.postgres;
+
+import static org.assertj.core.api.Assertions.assertThat;
+
+import java.util.concurrent.atomic.AtomicInteger;
+
+import org.elasticsearch.test.ESTestCase;
+import org.junit.Test;
+
+import io.netty.buffer.ByteBuf;
+import io.netty.buffer.Unpooled;
+import io.netty.channel.embedded.EmbeddedChannel;
+
+public class DelayableWriteChannelTest extends ESTestCase {
+
+    @Test
+    public void test_delayed_writes_are_released_on_close() throws Exception {
+        var channel = new DelayableWriteChannel(new EmbeddedChannel());
+        channel.delayWrites();
+        ByteBuf buffer = Unpooled.buffer();
+        channel.write(buffer);
+        channel.close();
+        assertThat(buffer.refCnt()).isEqualTo(0);
+    }
+
+    @Test
+    public void test_can_add_and_unblock_from_different_threads() throws Exception {
+        AtomicInteger numMessages = new AtomicInteger(50);
+        EmbeddedChannel innerChannel = new EmbeddedChannel();
+        var channel = new DelayableWriteChannel(innerChannel);
+        try {
+            channel.delayWrites();
+            var thread1 = new Thread(() -> {
+                while (numMessages.decrementAndGet() >= 0) {
+                    ByteBuf msg = channel.alloc().buffer();
+                    msg.setInt(0, 1);
+                    channel.write(msg);
+                }
+            });
+            var thread2 = new Thread(() -> {
+                while (numMessages.get() > 0) {
+                    channel.writePendingMessages();
+                    channel.delayWrites();
+                }
+            });
+            thread1.start();
+            thread2.start();
+
+            thread1.join();
+            thread2.join();
+
+            channel.writePendingMessages();
+            channel.flush();
+            assertThat(innerChannel.outboundMessages()).hasSize(50);
+        } finally {
+            innerChannel.finishAndReleaseAll();
+        }
+    }
+}
diff --git a/server/src/test/java/io/crate/protocols/postgres/PostgresWireProtocolTest.java b/server/src/test/java/io/crate/protocols/postgres/PostgresWireProtocolTest.java
index 927c436046..54f0c1cf2f 100644
--- a/server/src/test/java/io/crate/protocols/postgres/PostgresWireProtocolTest.java
+++ b/server/src/test/java/io/crate/protocols/postgres/PostgresWireProtocolTest.java
@@ -139,7 +139,7 @@ public class PostgresWireProtocolTest extends CrateDummyClusterServiceUnitTest {
             readKeyData(channel);
             readReadyForQueryMessage(channel);
             Messages.writeCString(buffer, ";".getBytes(StandardCharsets.UTF_8));
-            ctx.handleSimpleQuery(() -> {}, buffer, channel);
+            ctx.handleSimpleQuery(buffer, new DelayableWriteChannel(channel));
         } finally {
             buffer.release();
         }
@@ -865,7 +865,9 @@ public class PostgresWireProtocolTest extends CrateDummyClusterServiceUnitTest {
         try {
             // the actual statements don't have to be valid as they are not executed
             Messages.writeCString(query, statements.getBytes(StandardCharsets.UTF_8));
-            ctx.handleSimpleQuery(() -> {}, query, channel);
+            DelayableWriteChannel delayChannel = new DelayableWriteChannel(channel);
+            ctx.handleSimpleQuery(query, delayChannel);
+            delayChannel.writePendingMessages();
         } finally {
             query.release();
         }
diff --git a/server/src/test/java/io/crate/protocols/postgres/ResultSetReceiverTest.java b/server/src/test/java/io/crate/protocols/postgres/ResultSetReceiverTest.java
index 81bcdcad6f..2b2f23035a 100644
--- a/server/src/test/java/io/crate/protocols/postgres/ResultSetReceiverTest.java
+++ b/server/src/test/java/io/crate/protocols/postgres/ResultSetReceiverTest.java
@@ -35,6 +35,7 @@ import org.mockito.Answers;
 
 import io.crate.auth.AccessControl;
 import io.crate.data.Row1;
+import io.crate.protocols.postgres.DelayableWriteChannel.DelayedWrites;
 import io.crate.protocols.postgres.types.PGTypes;
 import io.crate.types.DataTypes;
 import io.netty.buffer.ByteBuf;
@@ -50,9 +51,12 @@ public class ResultSetReceiverTest {
     public void testChannelIsPeriodicallyFlushedToAvoidConsumingTooMuchMemory() {
         Channel channel = mock(Channel.class, Answers.RETURNS_DEEP_STUBS);
         when(channel.isWritable()).thenReturn(true);
+        DelayableWriteChannel delayableWriteChannel = new DelayableWriteChannel(channel);
+        DelayedWrites delayWrites = delayableWriteChannel.delayWrites();
         ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
             "select * from t",
-            channel,
+            delayableWriteChannel,
+            delayWrites,
             AccessControl.DISABLED,
             Collections.singletonList(PGTypes.get(DataTypes.INTEGER)),
             null
@@ -67,9 +71,12 @@ public class ResultSetReceiverTest {
     @Test
     public void test_channel_is_flushed_if_not_writable_anymore() {
         Channel channel = mock(Channel.class, Answers.RETURNS_DEEP_STUBS);
+        DelayableWriteChannel delayableWriteChannel = new DelayableWriteChannel(channel);
+        DelayedWrites delayWrites = delayableWriteChannel.delayWrites();
         ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
             "select * from t",
-            channel,
+            delayableWriteChannel,
+            delayWrites,
             AccessControl.DISABLED,
             Collections.singletonList(PGTypes.get(DataTypes.INTEGER)),
             null
@@ -100,9 +107,12 @@ public class ResultSetReceiverTest {
                 return promise;
             }
         };
+        DelayableWriteChannel delayableWriteChannel = new DelayableWriteChannel(channel);
+        DelayedWrites delayWrites = delayableWriteChannel.delayWrites();
         ResultSetReceiver resultSetReceiver = new ResultSetReceiver(
             "select * from t",
-            channel,
+            delayableWriteChannel,
+            delayWrites,
             AccessControl.DISABLED,
             Collections.singletonList(PGTypes.get(DataTypes.INTEGER)),
             null

```
