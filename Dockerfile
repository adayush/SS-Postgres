FROM python:3.9-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /home

COPY requirements.txt /home/requirements.txt

RUN pip install -r requirements.txt

WORKDIR /home/backend
