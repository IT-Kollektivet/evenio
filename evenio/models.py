from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Category(models.Model):
    """ A category """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=64)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('title',)

    def natural_key(self):
        return (self.id, self.title)


class Event(models.Model):
    """ A event """
    title = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=64)
    
    starts = models.DateTimeField() # TODO: This should be a list of times!
    ends = models.DateTimeField(null=True, blank=True) # TODO: This should be a list of times!

    venue_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)

    categories = models.ManyToManyField(Category)
    
    description = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, null=True, blank=True)
    owner_anonymous = models.CharField(max_length=255, null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)

    # Allow:
    rsvp = models.BooleanField(default=True)
    rsvp_anonymous = models.BooleanField(default=True)
    comments_before = models.BooleanField(default=True)
    comments_after = models.BooleanField(default=True)
    comments_anonymous_before = models.BooleanField(default=True)
    comments_anonymous_after = models.BooleanField(default=True)

    canceled = models.BooleanField(default=False)
    changed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-starts',)

    def get_categories_string(self):
        """Admin list"""
        return ", ".join([c.title for c in self.categories.all()])
    get_categories_string.short_description = _("Categories")
    


def generate_test_data():
    from datetime import datetime, timedelta
    from random import choice, randint
    dates = 300
    now = datetime.now()
    from django.template.defaultfilters import slugify
    
    categories = ["Food", "Concert", "Party", "Talk", "Poetry"]
    
    names = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    names = slugify(names).split("-")
    
    print names
    
    for c in categories:
        cat = Category(title=c, slug=slugify(c))
        cat.save()
    
    categories = Category.objects.all()
    
    for _ in range(1000):
        
        e = Event()
        e.title = "%s %s" % (choice(names), choice(names))
        e.title = e.title[0].upper() + e.title[1:]
        e.slug = slugify(e.title)
        e.starts = now + timedelta(days=randint(0, dates))
        e.price = choice([0,100,200,20,30,50])
        e.description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
        e.save()
        for c in categories.order_by('?')[:randint(1,3)]:
            e.categories.add(c)
        

        

