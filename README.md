evenio
======

web site for evenio.dk

**Folder structure**:
```
evenio/ <- Django app for creating and managing events
testproject/ <- A test project with code examples on how to set up a proper project by benjaoming
eveniodk/ <- What is to become evenio.dk website (using the Django evenio app)
```
Django-guide: https://docs.djangoproject.com/en/dev/topics/install/

Start web server:
```shell
./manage.py runserver
```

Populate db:
```shell
./manage.py shell
>>> from evenio import models
>>> models.generate_test_data()
```

If this is the first time you are generating a database then you need to sync and migrate data schemes from the evenio app to your site (eveniodk/)
```shell
./manage.py syncdb
/.manage.py migrate
```
Now you can populate the db as described above.

Upgrade your Django installation (using [pip](http://pypi.python.org/pypi/pip)):
```shell
pip install django django-guardian easy_thumbnails south django-tastypie --upgrade
```