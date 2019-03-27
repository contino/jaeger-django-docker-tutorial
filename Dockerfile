FROM python:3-alpine
MAINTAINER Carlos Nunez <carlos@contino.io>

ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install django psycopg2 "opentracing<2" "django_opentracing==0.1.20" jaeger-client
