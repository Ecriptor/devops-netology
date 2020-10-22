FROM amazoncorretto
ADD https://pkg.jenkins.io/redhat-stable/jenkins.repo /etc/yum.repos.d/
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key && \
    yum install -y jenkins
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]
