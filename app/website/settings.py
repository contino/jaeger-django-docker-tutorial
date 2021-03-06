"""
Django for website project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/

For the full list of and their values, see
https://docs.djangoproject.com/en/2.1/ref/
"""

import os, yaml, time
from . import database, tracing
from django.core.exceptions import ImproperlyConfigured


def get_from_django_config(key):
    try:
        global django_configs
        value = django_configs[key]
        if value == "True":
            value = True
        elif value == "False":
            value = False
        return value
    except KeyError:
        raise ImproperlyConfigured("Please define Django configuration parameter: " + key)
    except NameError:
        return None


def wait_for_config_file():
    max_attempts = 60
    for attempt in range(0, max_attempts):
        file = os.getenv("DJANGO_CONFIGURATION_FILE")
        if os.path.isfile(file):
            return
        if attempt == max_attempts:
            raise TimeoutError("Timed out while waiting for config to become available.")
        print("Waiting for " + file + " to become available...")
        time.sleep(1)


def initialize_config():
    wait_for_config_file()
    file_location = os.getenv("DJANGO_CONFIGURATION_FILE")
    with open(file_location) as config_file:
        return yaml.load(config_file.read())


django_configs = initialize_config()
for django_config_key in [
        'SECRET_KEY',
        'DEBUG',
        'ALLOWED_HOSTS',
        'ROOT_URLCONF',
        'INSTALLED_APPS',
        'MIDDLEWARE',
        'LANGUAGE_CODE',
        'TIME_ZONE',
        'USE_I18N',
        'USE_L10N',
        'USE_TZ',
        'STATIC_URL',
        'OPENTRACING_TRACE_ALL',
        'OPENTRACING_TRACED_ATTRIBUTES',
        'OPENTRACING_TRACER_CALLABLE',
        'DATABASES',
        'JAEGER_SERVICE_NAME',
        'JAEGER_AGENT_HOST',
        'JAEGER_AGENT_PORT',
]:
    locals()[django_config_key] = get_from_django_config(django_config_key)

database.wait_for_database_or_raise(
    database_host=DATABASES['default']['HOST'],
    database_port=DATABASES['default']['PORT'],
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
