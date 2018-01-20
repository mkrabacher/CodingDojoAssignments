# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now=True)