FROM python:3
MAINTAINER Carlos Nunez <carlos@contino.io>

ENV PYTHONUNBUFFERED 1
RUN pip install django psycopg
