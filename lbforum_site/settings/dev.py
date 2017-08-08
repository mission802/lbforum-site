from .base import *  # NOQA

DEBUG = True
THUMBNAIL_DEBUG = True
DEBUG_WORKFLOW = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    import debug_toolbar  # NOQA
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
except Exception as e:
    pass
