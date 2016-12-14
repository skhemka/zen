from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from address.models import AddressField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

#using address from github applicaiton (check back)
class Location(models.Model):
    address = AddressField()
    time_to_campus = models.IntegerField(null=True, blank=True)

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Producer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=200)
    on_campus = models.BooleanField()

class Event(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Preference(models.Model):
    # user -> {category: weight}
    # tries to emulate the above map in database terms
    #TODO: check this for errors in data modelling
    consumer = models.OneToOneField(Consumer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class Subscription(models.Model):
    #if errors of lenght occur check here
    url = models.URLField(max_length=400)
    consumer = models.ForeignKey(Consumer,on_delete=models.CASCADE)

#calendar is not here because the data is never stored on the app
