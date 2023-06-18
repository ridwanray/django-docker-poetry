# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat \
    build-essential libpq-dev \
    && pip install Pillow

COPY ./requirements ./requirements

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements/dev.txt

# Set the environment variables
ENV DJANGO_READ_DOT_ENV_FILE=True
ENV DOT_ENV_FILE=/app/.env

COPY . /app

