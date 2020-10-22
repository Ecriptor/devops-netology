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
