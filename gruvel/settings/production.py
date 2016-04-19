from .base import *


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
