# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, redirect

def index(request):
    if 'log' not in request.session:
        request.session['log'] = []
    
    return render(request, 'session_app/index.html')

def process(request):
    if request.method == 'POST':
        word = request.POST['word']
        color = request.POST['color']
        if request.POST['big'] == 'on':
            big = 250
        else:
            big = 100
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        tup = (word, color, big)
        request.session['log'].append({
            'word':word,
            'color':color,
            'big':big,
            'time':time
        })
        request.session['log'] = request.session['log']
    return redirect('/')

def clear(request):
    request.session['log'] = []
    return redirect('/')