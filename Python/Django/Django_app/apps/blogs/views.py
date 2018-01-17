# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs. *grammar"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def edit(request, number):
    response = "i edit blog number: " + number
    return HttpResponse(response)

def delete(request, number):
    print 'hellp'
    return redirect('/')

def show(request, number):
    response = "placeholder for blog number: " + number
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')