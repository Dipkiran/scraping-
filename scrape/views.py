from django.shortcuts import render

from scrape import  *
import datetime
from .models import *
time = datetime.datetime.now()
first()

def index(request):
    newtime  = datetime.datetime.now()
    diff = newtime - time
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print hours, minutes, seconds
    if hours != 0 and hours % 6 == 0:
        first()
    all_data = job.objects.values('link', 'title')
    context = {
        'all_data': all_data,
    }
    return render(request, "index.html", context)