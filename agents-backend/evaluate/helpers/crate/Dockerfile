FROM maven:3.9-eclipse-temurin-24

# Install necessary tools
RUN apt-get update && apt-get install -y \
    git \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /repo

# Set working directory
WORKDIR /repo

# Inject toolchains.xml to satisfy Maven plugins system-wide
RUN mkdir -p /root/.m2 && \
    echo '<toolchains><toolchain><type>jdk</type><provides><version>24.0.2</version><vendor>temurin</vendor></provides><configuration><jdkHome>/opt/java/openjdk</jdkHome></configuration></toolchain></toolchains>' > /usr/share/maven/conf/toolchains.xml && \
    cp /usr/share/maven/conf/toolchains.xml /root/.m2/toolchains.xml

# Set environment variables
ENV MAVEN_OPTS="-Xmx4g -XX:+UseG1GC"

# Default command
CMD ["/bin/bash"]
