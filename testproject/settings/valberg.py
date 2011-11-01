from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dbevenio',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Django-debug-toolbar related:
    # read moar at: http://pypi.python.org/pypi/django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)


# Django-extensions related
    # read moar at: http://packages.python.org/django-extensions/
INSTALLED_APPS += ('django_extensions',)
