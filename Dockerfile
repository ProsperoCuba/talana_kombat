FROM python:3.8.12-alpine3.15

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /app/requirements.txt
RUN pip install -U pip setuptools
RUN pip install -r /app/requirements.txt
COPY . /app

# comment if you do not want to run test on build stage
RUN pytest -q tests/test.py
