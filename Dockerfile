FROM python:3-alpine
MAINTAINER Carlos Nunez <carlos@contino.io>

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev git
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
