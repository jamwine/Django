# Base image
FROM python:3.9.6-alpine

# Adding Labels
LABEL VERSION="1.0"
LABEL MAINTAINER="JAMWINE"

# Create the working directory in docker container
RUN mkdir /django_web

# Set the working directory
WORKDIR /django_web

# Copy requirements file to the container
COPY requirements.txt /django_web/requirements.txt

# Set Environment Variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
#     PYTHONPATH=/django_web
#     DJANGO_SETTINGS_MODULE=my_project.settings

# Install dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del .tmp-build-deps

# Copy the project code to the container
COPY ./django_web /django_web

# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static
# RUN adduser -D user
# RUN chown -R user:user /vol/
# RUN chmod -R 755 /vol/web
# USER user