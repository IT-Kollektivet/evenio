evenio
======

web site for evenio.dk
Start web server:
./manage.py runserver

Populate db:
./manage.py shell
>>> from evenio import models
>>> models.generate_test_data()