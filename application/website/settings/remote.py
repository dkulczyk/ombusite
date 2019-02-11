import os
from website.settings.base import *
import http.client

def get_local_ip():
    try:
        connection = http.client.HTTPConnection("169.254.169.254", timeout=2)
        connection.request('GET', '/latest/meta-data/local-ipv4')
        response = connection.getresponse()
        return response.read().decode('utf-8')
    except Exception:
        return None

DATABASES['default']['NAME'] = os.environ.get('DATABASE_NAME', None)
DATABASES['default']['USER'] = os.environ.get('DATABASE_USER', None)
DATABASES['default']['PASSWORD'] = os.environ.get('DATABASE_PASSWORD', None)
DATABASES['default']['HOST'] = os.environ.get('DATABASE_ENDPOINT', None)
DATABASES['default']['PORT'] = '5432'
ALLOWED_HOSTS = ['', get_local_ip(), os.environ.get('DOMAIN', None)]
STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'

if os.getenv('ENVIRONMENT_TYPE', None) in ('qa', 'staging'):
    MIDDLEWARE = ['basicauth.middleware.BasicAuthMiddleware',] + MIDDLEWARE
