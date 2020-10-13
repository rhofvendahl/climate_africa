"""
WSGI config for climate_africa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import environ
env = environ.Env(
    DEBUG=(bool, False)
) # should maybe change this when debugging
environ.Env.read_env()

from django.core.wsgi import get_wsgi_application

django_settings_module = env('DJANGO_SETTINGS_MODULE')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

application = get_wsgi_application()
