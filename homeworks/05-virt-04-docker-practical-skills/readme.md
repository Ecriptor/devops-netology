# Ответы на вопросы

## Задача 1


* Dockerfile
```
FROM centos:centos7
ADD http://github.com/erkin/ponysay/archive/master.tar.gz /
RUN yum check-update && \
    yum install -y texinfo python3 && \
    tar -xzf master.tar.gz && \
    cd ponysay-master && \
    ./setup.py install --freedom=partial && \
     rm -rf /master.tar.gz /ponysay-master
RUN yum clean all
ENTRYPOINT ["/usr/bin/ponysay"]
CMD ["Hey, netology"]

```
* Screenshot<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/ex3_ponysay_screenshot.png)

* Ссылка на репозиторий с образом
[https://hub.docker.com/r/ecriptor/ponysay-centos](https://hub.docker.com/r/ecriptor/ponysay-centos)


## Задача 2

* Ссылка на репозиторий с образом
[https://hub.docker.com/r/ecriptor/jenkins](https://hub.docker.com/r/ecriptor/jenkins)

* Dockerfile для amazoncorreto
```
FROM amazoncorretto
ADD https://pkg.jenkins.io/redhat-stable/jenkins.repo /etc/yum.repos.d/
RUN rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key && \
    yum install -y jenkins
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]
```
Скриншот логов запущенного контейнера<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/logs_jenkins_v1.png)
Скриншот опубликованного приложения<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/jenkins_app_1.png)

Сам контейнер на основе amazoncorreto можно запустить вот так!
```
docker run -d --name jenkins-srv -p 8080:8080 ecriptor/jenkins:ver1
``` 


* Dockerfile для ubuntu
```
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
```
Скриншот логов запущенного контейнера<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/logs_jenkins_v2.png)
Скриншот опубликованного приложения<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/jenkins_app_2.png)

Сам контейнер на основе ubuntu можно запустить вот так!
```
docker run -d --name jenkins-srv -p 8080:8080 ecriptor/jenkins:ver2
``` 

## Задача 3

* Dockerfile с npm приложением
```
FROM node
WORKDIR "/nodejs"
RUN git clone https://github.com/simplicitesoftware/nodejs-demo.git . && \
    npm install
EXPOSE 3000
CMD ["npm", "start", "0.0.0.0"]
```
Скриншот списка docker сетей<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/ex3_docker_network.png)

Скриншот вызова утилиты curl<br>
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/ex3_docker_curl.png)

