from __future__ import absolute_import, unicode_literals

from .production import *
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# django-lockdown Settings https://github.com/Dunedan/django-lockdown
INSTALLED_APPS += ('lockdown',)
MIDDLEWARE += ('lockdown.middleware.LockdownMiddleware',)
LOCKDOWN_URL_EXCEPTIONS = (r'^/admin',)
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'
LOCKDOWN_PASSWORDS = (os.environ['LOCKDOWN_PASSWORD'],)
