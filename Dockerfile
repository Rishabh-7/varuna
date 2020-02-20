FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /varuna

WORKDIR /varuna

ADD . /varuna/

RUN pip3 install -r requirements.txt
