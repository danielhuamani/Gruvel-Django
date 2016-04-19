from .base import *

DEBUG = True

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS')

STATIC_ROOT = ''

STATIC_URL = ENV.get('STATIC_URL')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = ENV.get('MEDIA_URL')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
