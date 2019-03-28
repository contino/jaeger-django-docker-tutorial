import os, django_opentracing
from jaeger_client import Config
from django.conf import settings


def tracer():
    config = Config(
        config={  # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent': {
                'reporting_host': settings.JAEGER_AGENT_HOST,
                'reporting_port': settings.JAEGER_AGENT_PORT,
            }
        },
        service_name=settings.JAEGER_SERVICE_NAME)
    return config.initialize_tracer()
