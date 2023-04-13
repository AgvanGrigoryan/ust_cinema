"""
WSGI config for ust_cinema project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
env_path = Path('..', '.env')
load_dotenv(env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ust_cinema.settings')

application = get_wsgi_application()
