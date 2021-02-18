# Pull base image
FROM python:3.7

ENV http_proxy http://10.1.1.35:8080
ENV https_proxy http://10.1.1.35:8080

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
