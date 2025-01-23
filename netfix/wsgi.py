"""
WSGI config for netfix project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'netfix' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netfix.settings')

# Create the WSGI application
application = get_wsgi_application()

