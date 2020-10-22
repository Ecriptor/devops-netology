FROM ubuntu:latest
ADD https://pkg.jenkins.io/debian-stable/jenkins.io.key /
RUN apt-get update && \
    apt-get install -y gnupg ca-certificates && \
    apt-key add /jenkins.io.key && \
    sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list' && \
    apt-get update && \
    apt-get install -y jenkins && \
    apt-get clean
CMD ["systemctl", "start", "jenkins"]
