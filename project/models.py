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
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    producer = models.ForeignKey(Producer,on_delete=models.PROTECT)

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
