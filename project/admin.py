from django.contrib import admin

from .models import Category, Location, Consumer, Producer, Event, Preference, Subscription

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Consumer)
admin.site.register(Producer)
admin.site.register(Event)
admin.site.register(Preference)
admin.site.register(Subscription)
