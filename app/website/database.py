import os
import socket
import time
import django.conf as conf


def is_database_available(database_host, database_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock.connect_ex((database_host, database_port)) == 0


def wait_for_database(database_host, database_port, retry_limit_seconds=60):
    """ Waits for the database to become available. """
    """ TODO: Use logging instead of print functions. """
    for attempt in range(0, retry_limit_seconds - 1):
        if is_database_available(database_host, database_port):
            return True

        print("Waiting for DB at %s:%d (attempt %d of %d)" % (database_host, database_port, attempt,
                                                              retry_limit_seconds))
        time.sleep(1)

    return False


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


def configure_database():
    conf.settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
        }
    }

    for env_var in ['NAME', 'USER', 'PASSWORD', 'HOST', 'PORT']:
        env_var_to_get = 'DATABASE_' + env_var
        if env_var_to_get not in os.environ:
            raise NameError("Please define %s in your environment." % env_var_to_get)

        conf.settings.DATABASES['default'][env_var] = os.getenv('DATABASE_' + env_var)
    if not wait_for_database(os.getenv('DATABASE_HOST'), int(os.getenv('DATABASE_PORT'))):
        raise TimeoutError("Unable to connect to the database.")
