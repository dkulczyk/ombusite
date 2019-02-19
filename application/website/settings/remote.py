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
DOMAIN = os.environ.get('DOMAIN', None)

if os.getenv('ENVIRONMENT_TYPE', None) in ('qa', 'staging'):
    MIDDLEWARE = ['basicauth.middleware.BasicAuthMiddleware',] + MIDDLEWARE



# Temporary debug toolbar.
DEBUG = True
INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware',] + MIDDLEWARE

def show_toolbar_callback(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': None,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar_callback,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    # 'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    # 'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]
