"""
WSGI config for personal_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os
import mod_wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'check_apache.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.handlers.modwsgi import check_password