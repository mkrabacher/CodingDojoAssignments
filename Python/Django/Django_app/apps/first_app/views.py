# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def test(request):
    response = "testing testing 1,2,3"
    return HttpResponse(response)
