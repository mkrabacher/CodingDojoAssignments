# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from datetime import datetime
import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'users/index.html', context)

def success(request):
    context = {
        'users':User.objects.all(),
        'curr_user':User.objects.get(id=request.session['curr_user_id'])
    }
    return render(request, 'users/success.html', context)

def registerUser(request):
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        email = request.POST['email']
        birthday = request.POST['birthday']
        password = request.POST['password']
        pw_conf = request.POST['pw_conf']

        errors = User.objects.validate(request.POST)
        print 'errors', errors
        if len(errors) > 0:
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            User.objects.create(fName=fName, lName=lName, email=email,birthday=birthday, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
            messages.add_message(request, messages.INFO, 'Success. Now log in.')
            return redirect('/')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.add_message(request, messages.INFO, 'Email does not exist. you suck.')
            return redirect('/')

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['curr_user_id'] = user.id
            return redirect('/success')