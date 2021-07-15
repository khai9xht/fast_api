FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install git vim -y

RUN apt-get install -y python3-pip python3-dev -y \
	&& cd /usr/local/bin \
	&& ln -s /usr/bin/python3 python

WORKDIR /home

RUN mkdir fast_api

COPY ./ /home/fast_api

RUN pip3 install --upgrade pip

WORKDIR /home/fast_api

RUN pip install --no-cache-dir -r requirements.txt
