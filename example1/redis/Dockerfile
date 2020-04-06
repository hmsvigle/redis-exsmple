FROM ubuntu:18.04

ARG  VERSION=5.0.8

ENV  REDIS_HOME=/etc/redis/ 
ENV  PATH=$PATH:${REDIS_HOME}:${REDIS_HOME}/src

RUN  set -x && \
     apt-get update

RUN  set -x && \   
     apt-get install -y wget build-essential 

WORKDIR ${REDIS_HOME}

RUN  set -x && \
     wget -O /etc/redis-${VERSION}.tar.gz http://download.redis.io/releases/redis-${VERSION}.tar.gz && \
     tar -xzvf /etc/redis-${VERSION}.tar.gz -C ${REDIS_HOME} && \
     mv ${REDIS_HOME}/redis-${VERSION}/* ${REDIS_HOME} && \
     rm -rf ${REDIS_HOME}/redis-${VERSION} *.tar.gz

RUN  sed -i 's/protected-mode yes/protected-mode no/' ${REDIS_HOME}/redis.conf && \
     sed -i 's/bind 127.0.0.1/\#bind 127.0.0.1/' ${REDIS_HOME}/redis.conf

RUN  make

EXPOSE 6379 

ENTRYPOINT ["redis-server", "--protected-mode", "no" ]
