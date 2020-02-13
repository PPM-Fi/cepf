"""
Django settings for cepf project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yefr1+*(%_3fd^v&x$o^1g%3q1p!!#$%db75gc!3w8b)@g%xhh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cepf',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

# PWA settings

PWA_APP_DEBUG_MODE = True

PWA_APP_NAME = 'CEPF'
PWA_APP_DESCRIPTION = "Nottinghamshire Community Engagement Peformance Framework"
PWA_APP_THEME_COLOR = '#03a9f4'
PWA_APP_BACKGROUND_COLOR = '#03a9f4'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    { 'src': '/static/images/icons/icon-512x512.png', 'sizes': '512x512' },
    { 'src': '/static/images/icons/icon-384x384.png', 'sizes': '384x384' },
    { 'src': '/static/images/icons/icon-192x192.png', 'sizes': '192x192' },
    { 'src': '/static/images/icons/icon-152x152.png', 'sizes': '152x152' },
    { 'src': '/static/images/icons/icon-144x144.png', 'sizes': '144x144' },
    { 'src': '/static/images/icons/icon-128x128.png', 'sizes': '128x128' },
    { 'src': '/static/images/icons/icon-96x96.png', 'sizes': '96x96' },
    { 'src': '/static/images/icons/icon-72x72.png', 'sizes': '72x72' },
]
PWA_APP_ICONS_APPLE = [
    { 'src': '/static/images/icons/icon-512x512-apple.png', 'sizes': '512x512' },
    { 'src': '/static/images/icons/icon-384x384-apple.png', 'sizes': '384x384' },
    { 'src': '/static/images/icons/icon-192x192-apple.png', 'sizes': '192x192' },
    { 'src': '/static/images/icons/icon-152x152-apple.png', 'sizes': '152x152' },
    { 'src': '/static/images/icons/icon-144x144-apple.png', 'sizes': '144x144' },
    { 'src': '/static/images/icons/icon-128x128-apple.png', 'sizes': '128x128' },
    { 'src': '/static/images/icons/icon-96x96-apple.png', 'sizes': '96x96' },
    { 'src': '/static/images/icons/icon-72x72-apple.png', 'sizes': '72x72' },
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
