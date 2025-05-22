# Defined base image, usually search in docker hub
# FROM is a directive
# FROM ubuntu:18.04
FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

ARG TEXT_EDITOR=nano

# Directive RUN is to execute commands into the container
RUN apt-get update && apt-get install -y \
    python3 curl $TEXT_EDITOR

# Directive COPY is to copy files and introducing into container
COPY . /app

WORKDIR /app