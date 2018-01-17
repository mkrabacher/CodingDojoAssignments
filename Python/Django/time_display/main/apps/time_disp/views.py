# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request, 'time_disp/index.html', context)