import os

from django.core.exceptions import ImproperlyConfigured

def get_secret(secret_name):
    if os.getenv(secret_name):
        return os.getenv(secret_name)
    else:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)