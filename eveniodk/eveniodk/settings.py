# -*- coding: utf-8 -*-
from os import path as os_path
PROJECT_PATH = os_path.abspath(os_path.split(__file__)[0])

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('xyz', 'benjamin@maitri.dk'),('dotnetcarpenter', 'jon@maitri.dk'),('mortengf', 'morten@maitri.dk'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test.db', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'da-dk'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os_path.join(PROJECT_PATH, "media")
MEDIA_URL = '/media/'
STATIC_ROOT = os_path.join(PROJECT_PATH, "static")
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os_path.join(PROJECT_PATH, "static_files"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0=t-72*-c&w2%rjk$07!f!zvo&*a$40@1sfq!n16otdj7vnl2#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
# 'userena.middleware.UserenaLocaleMiddleware'
)

AUTHENTICATION_BACKENDS = (
#    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ROOT_URLCONF = 'eveniodk.urls'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',
    'evenio',
    'guardian',
 #   'userena',
    'easy_thumbnails',
 #   'evenioprofiles',
 #   'bootstrap_toolkit',
    'south',
    'tastypie',
    'eveniodk'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# the below line is used by userena which don't use at the moment
#AUTH_PROFILE_MODULE = 'evenioprofiles.EvenioProfile'
ANONYMOUS_USER_ID = -1
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

EMAIL_USE_TLS = True
EMAIL_HOST = '<FILL_IN>'
EMAIL_HOST_USER = '<FILL_IN>'
EMAIL_HOST_PASSWORD = '<FILL_IN>'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

print 'EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD MIGHT NEED TO BE FILLED IN.'