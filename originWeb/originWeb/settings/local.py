
from .base import *

import os
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': config('NAME'),
    'USER': config('USER'),
    'PASSWORD': config('PASSWORD'),
    'HOST': config('HOST'),
    'PORT': config('PORT', cast=int),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [BASE_DIR.child('static')]
STATICFILES_DIRS = [
    'originWeb/static',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
