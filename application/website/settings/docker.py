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
    # 'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    # 'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]
