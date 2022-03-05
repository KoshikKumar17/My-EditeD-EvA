FROM python:3.10-slim-buster

ENV PYTHON_VERSION 3.10.2
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /EvaMaria
WORKDIR /EvaMaria
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
