import os, django_opentracing
import django.conf as conf
from jaeger_client import Config

def tracer():
    config = Config(
        config={ # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=os.getenv('JAEGER_SERVICE_NAME'))
    return config.initialize_tracer()

def init_jaeger_tracer():
    """ Holy hell.
    Configuring this without abstracting it into website/settings.py was a nightmare.
    
    First, trying to install django_opentracing without version pinning lead
    to conflicts because jaeger-client (which we need) isn't compatible with
    opentracing>2. The documentation doesn't reference this, nor does
    it reference how to wire this up with Jaeger.

    Second, all of the documentation is incomplete. The environment variables
    below could only be found by looking for calls to `os.getenv` in the
    Python client source code.

    So far, I am not a fan of tracing...at least not with this library."""
    for env_var in ['JAEGER_SERVICE_NAME','JAEGER_AGENT_HOST','JAEGER_AGENT_PORT']:
        if env_var not in os.environ:
            raise NameError('Please define the "%s" environment variable.' % env_var)
    conf.settings.INSTALLED_APPS.append('django_opentracing')
    conf.settings.MIDDLEWARE.append('django_opentracing.OpenTracingMiddleware')
    conf.settings.OPENTRACING_TRACE_ALL = True
    conf.settings.OPENTRACING_TRACED_ATTRIBUTES = ['path', 'method']
    conf.settings.OPENTRACING_TRACER_CALLABLE = 'tracing.tracer'
