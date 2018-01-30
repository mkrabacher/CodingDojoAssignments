# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
from datetime import *



class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    wand_desc = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    house = models.CharField(max_length=255)

