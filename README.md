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