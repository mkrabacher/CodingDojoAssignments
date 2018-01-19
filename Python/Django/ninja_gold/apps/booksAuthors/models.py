# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    