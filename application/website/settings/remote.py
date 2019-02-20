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
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 15768000 # Trigger Strict-Transport-Security header.
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware', # View caching.
    'django.middleware.gzip.GZipMiddleware', # GZip.
    'htmlmin.middleware.HtmlMinifyMiddleware', # Minify HTML.
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', # View caching.
    'htmlmin.middleware.MarkRequestMiddleware', # View caching.
    'csp.middleware.CSPMiddleware',
]

if os.getenv('ENVIRONMENT_TYPE', None) in ('qa', 'staging'):
    MIDDLEWARE = ['basicauth.middleware.BasicAuthMiddleware',] + MIDDLEWARE

if os.getenv('ENVIRONMENT_TYPE', None) == 'production':
    GOOGLE_ANALYTICS_ID = 'UA-16055309-1'
