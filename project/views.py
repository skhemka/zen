from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

from project.models import *

# Create your views here.

def home(request):
    return render(request, 'project/home.html')

def getAllEvents(request):
    events = Event.objects.all()
    data = serializers.serialize("json",events)
    return HttpResponse(data,content_type="application/json")
