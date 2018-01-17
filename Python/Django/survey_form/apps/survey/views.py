# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/index.html')

def survey(request):
    if request.method == 'POST':
        request.session['context'] = {
            'name':request.POST['name'],
            'location':request.POST['loc'],
            'lang':request.POST['lang'],
            'comment':request.POST['comment']
        }
    return redirect('/show')

def show(request):
    return render(request, 'survey/show.html')