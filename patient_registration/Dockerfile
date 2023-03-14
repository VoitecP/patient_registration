# Base image
FROM python:3.8-slim-buster


# env variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

# setting work directory
WORKDIR /usr/src/app


# install psycopg2 dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --system --ignore-pipfile


# install dependencies Without Pienv package
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt


# Copy to path 
COPY . .


# lint
# flake8 errors not repaired 
# RUN flake8 --ignore=E501,F401 . 


# Port Exposing
EXPOSE 8000
