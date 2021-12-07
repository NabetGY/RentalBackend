"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from logging import DEBUG
from pathlib import Path
from corsheaders.defaults import default_headers
import os
import environ
from datetime import timedelta

env = environ.Env()

import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku

environ.Env.read_env()

DEBUG = env( 'DEBUG' )
SECRET_KEY = env( 'SECRET_KEY' )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path( __file__ ).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['localhost', 'lumayo-arrendamientos.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'core',
    'corsheaders',
    'users',
    'rooms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
   # Corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
''' CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8000',
    'http://192.168.101.5:8080',
] '''

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
            },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

''' import dj_database_url
 '''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5r70gcseie9d1',
        'USER': 'zfrjzubbdxwhbe',
        'PASSWORD': '131b705fcf5aea1685e838bd0a6bea83ceabcb637879dcbcf59f55985d9eed4b',
        'HOST': 'ec2-34-195-69-118.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

''' import dj_database_url

db_from_env = dj_database_url.config(default='ppostgres://zfrjzubbdxwhbe:131b705fcf5aea1685e838bd0a6bea83ceabcb637879dcbcf59f55985d9eed4b@ec2-34-195-69-118.compute-1.amazonaws.com:5432/d5r70gcseie9d1')
DATABASES['default'].update(db_from_env)
 '''
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

AUTH_USER_MODEL = 'users.UserProfile'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [ 'rest_framework.permissions.AllowAny' ],
    'DEFAULT_AUTHENTICATION_CLASSES':
        [ 'rest_framework_simplejwt.authentication.JWTAuthentication',]
}

cloud_name = env( 'cloud_name' )
api_key = env( 'api_key' )
api_secret = env( 'api_secret' )

cloudinary.config(
    cloud_name = cloud_name,
    api_key = api_key,
    api_secret = api_secret,
    secure = True
)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta( minutes = 10 ),
    'REFRESH_TOKEN_LIFETIME': timedelta( days = 1 ),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

# Configure Django App for Heroku.

django_heroku.settings(locals())
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
