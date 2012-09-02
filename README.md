evenio
======

web site for evenio.dk

Django-guide: https://docs.djangoproject.com/en/dev/topics/install/

Start web server:
```shell
```./manage.py runserver
```

Populate db:
```shell
./manage.py shell
>>> from evenio import models
>>> models.generate_test_data()
```