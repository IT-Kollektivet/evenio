from django.db import models

class NutGraf(models.Model):
    ''' the gist of a story, explaining the basics '''
    heading = models.CharField(max_length=64)
    content = models.TextField()
    def __unicode__(self):
        return self.heading