# Ответы на вопросы

## Задача 1

- **Docker контейнеры** для микросервисов (легко пересобирать если появились новые изменения в коде) и для того что не жалко


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
* Screenshot
![Screenshot](/homeworks/05-virt-04-docker-practical-skills/ex3_ponysay_screenshot.png)

* Ссылка на репозиторий с образом
[https://hub.docker.com/r/ecriptor/ponysay-centos](https://hub.docker.com/r/ecriptor/ponysay-centos)


## Задача 2

* Мой репозиторий на Docker Hub [https://hub.docker.com/r/ecriptor/netology-httpd](https://hub.docker.com/r/ecriptor/netology-httpd)

Сам контейнер можно запустить вот так!
```
docker run -d --name httpd -p 80:80 ecriptor/netology-httpd:v1
``` 


## Задача 3

**Запуск конетйнера с Centos и создание файла**
```
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker run -it -v /info:/share/info --name centos -d centos /bin/bash
8964cc42c1464ea2b9669a977d25a108874d96f460d53551fee14d3e4588776e
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker ps
CONTAINER ID        IMAGE                        COMMAND              CREATED             STATUS              PORTS                NAMES
8964cc42c146        centos                       "/bin/bash"          4 seconds ago       Up 4 seconds                             centos
270f21673cb3        ecriptor/netology-httpd:v1   "httpd-foreground"   10 hours ago        Up 10 hours         0.0.0.0:80->80/tcp   httpd
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker exec -it 8964cc42c146 /bin/bash
[root@8964cc42c146 /]# 
[root@8964cc42c146 /]# cd /share/info/
[root@8964cc42c146 info]# echo "This is File from centos-container" > /share/info/test_centos.txt
[root@8964cc42c146 info]# exit
```
**Создание файла на хостовой машине**
```
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# ll /info/test_centos.txt 
-rw-r--r-- 1 root root 35 сен 29 09:37 /info/test_centos.txt
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# cat /info/test_centos.txt 
This is File from centos-container
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# echo "This is File from host machine" > /info/test_host.txt
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# cat /info/* 
This is File from centos-container
This is File from host machine
```
**Запуск конетйнера с Ubuntu и просмотр файлов**
```
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker run -it -v /info:/info --name ubuntu -d ubuntu /bin/bash
c3fccfbc61976f8430daf2bf3e449b973b37d83e8bc10ba002a1a1cf764fb3ee
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker ps
CONTAINER ID        IMAGE                        COMMAND              CREATED             STATUS              PORTS                NAMES
c3fccfbc6197        ubuntu                       "/bin/bash"          5 seconds ago       Up 3 seconds                             ubuntu
8964cc42c146        centos                       "/bin/bash"          5 minutes ago       Up 5 minutes                             centos
270f21673cb3        ecriptor/netology-httpd:v1   "httpd-foreground"   10 hours ago        Up 10 hours         0.0.0.0:80->80/tcp   httpd
root@ecriptor-virtual-machine:/home/ecriptor/devops-netology/docker# docker exec -it c3fccfbc6197 /bin/bash
root@c3fccfbc6197:/# ll /info/
total 16
drwxr-xr-x 2 root root 4096 Sep 29 06:38 ./
drwxr-xr-x 1 root root 4096 Sep 29 06:39 ../
-rw-r--r-- 1 root root   35 Sep 29 06:37 test_centos.txt
-rw-r--r-- 1 root root   31 Sep 29 06:38 test_host.txt
root@c3fccfbc6197:/# cat /info/*
This is File from centos-container
This is File from host machine
root@c3fccfbc6197:/#
```

