# Evenio

1. Setup
    1. Settings explained
        1. What?
        1. Why?
        1. How?
    1. Default
        1. Requires
        1. Setup
    1. Valbergs setup
        1. Requires
        1. Setup
        1. About

## Setup

### Settings explained
#### What?
Instead of having one huge settings file. we're trying a different approach.
The settings.py has now been transformed into a directory, or actually better
yet, a python module. That means that all settings files reside in settings/.

* **\__init__.py** contains the basic settings which are shared by all setting
  implementations.

 * **production.py** contains everything specific for production, this can be
   INSTALLED_APPS += ('gunicorn',) and such things as server specific database
   settings.

 * **<developer_name>.py** contains everything a specific developer wants. For
   instance, valberg uses django_debug_toolbar and django_extensions. If a
   developer wants to use some specific database software while developing,
   then that is entirely possible.

#### Why?
Not every developer is alike ;)

#### How?
So how does one use these settings? Simple, run them like this:

    python manage.py runserver --settings settings.<settings name>

For instance, to run valbergs settings run the development server using
django-extensions' runserver_plus like this:

    python manage.py runserver_plus --settings settings.valberg

Collecting static files on production server:

    python manage.py collectstatic --settings settings.production

and so on.

### Default
#### Requires
* Django==1.3.1
* South==0.7.3

#### Setup

    pip install -r requirements/default.txt

### Valbergs setup
#### Requires
Same as base, and:

* django-debug-toolbar==0.8.5
* django-extensions==0.7.1
* Werkzeug==0.8.1

#### Setup

    pip install -r requirements/valberg.txt

