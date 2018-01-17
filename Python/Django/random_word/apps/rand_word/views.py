# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
        request.session['str'] = get_random_string(length=14)
    else:
        request.session['attempt'] += 1

    return render(request, 'rand_word/index.html')

def generate(request):
    request.session['str'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    request.session['str'] = get_random_string(length=14)
    request.session['attempt'] = 0

    return redirect('/')
