from __future__ import unicode_literals

from django.db import models

from address.models import AddressField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

#using address from github applicaiton (check back)
class Location(models.Model):
    address = AddressField()
    time_to_campus = models.IntegerField(default=0)

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(default=0)

class 
