from __future__ import unicode_literals

from datetime import date

from django.db import models

class job(models.Model):
    link = models.CharField(blank=True, max_length=200)
    title = models.CharField(blank=True, max_length=200)

