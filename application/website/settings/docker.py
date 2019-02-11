from .base import *

DEBUG = True

DATABASES['default']['USER'] = 'root'
DATABASES['default']['PASSWORD'] = 'secret'
DATABASES['default']['HOST'] = 'db'

ALLOWED_HOSTS = ['localhost']

INTERNAL_IPS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

if DEBUG and 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',] + MIDDLEWARE

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': None
}