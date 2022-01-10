from .settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'grupo01',
        'USER' : 'grupo01',
        'PASSWORD' : 'grupo01',
        'DEFAULT-CHARACTER-SET' : 'utf8',
        'HOST' : 'icf233.c5d4mi2dthpc.us-east-1.rds.amazonaws.com',
        'PORT' : '3306',
        'TEST': {
            'NAME': 'grupo01_test',
        }
    },
}

STATIC_ROOT="/home/fbahamondes96/dpalimentos/static"

DEBUG=False

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

SECRET_KEY=os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']
USE_X_FORWARDED_HOST=True
USE_X_FORWARDED_PORT=True

INSTALLED_APPS += ('corsheaders',)
MIDDLEWARE += ('corsheaders.middleware.CorsMiddleware',)
CORS_ORIGIN_ALLOW_ALL = True


