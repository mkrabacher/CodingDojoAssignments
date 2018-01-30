# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from models import *
from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    start = models.TimeField('%H:%M')
    end = models.TimeField('%H:%M')
    spots = models.IntegerField()
    total_spots = models.IntegerField()
    students = models.ManyToManyField(User, through="rating")
    teacher = models.ForeignKey(User, related_name='teaching')

class Rating(models.Model):
    score = models.IntegerField()
    comment = models.CharField(max_length=255)
    rated_class = models.ForeignKey(Class, related_name='ratings_given')
    rater = models.ForeignKey(User, related_name='rated_classes')
