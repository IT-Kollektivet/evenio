# coding:utf-8
'''
An calendar application
'''

from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm


class UserProfile(models.Model):
    """ A verified users profile """
    user = models.ForeignKey(User) # User from auth framework
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=75)
    website = models.URLField(verify_exists=False, max_length=200, blank=True,
                              null=True)
    description = models.TextField()
    verified = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

