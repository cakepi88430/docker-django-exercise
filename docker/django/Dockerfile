# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./src/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./src /code/