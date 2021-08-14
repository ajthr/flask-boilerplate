FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app /app

ENV FLASK_ENV development
