# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from datetime import datetime
from random import randint
import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

def index(request):
    request.session.clear()
    context = {
        'users':User.objects.all(),
        'regForm':RegistrationForm(),
        'loginForm':LoginForm()
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
        response_form = RegistrationForm(request.POST)
        if response_form.is_valid():
            name = response_form.cleaned_data['name']
            email = response_form.cleaned_data['email']
            wand_desc = response_form.cleaned_data['wand_desc']

        password =response_form.cleaned_data['password']
        pw_conf = response_form.cleaned_data['confirm_password']
        if password != pw_conf:
            response_form.errors['password_match'] = "Your passwords don't match. Learn to type better"
        try:
            User.objects.get(email=email)
            response_form.errors['password_match'] = "Email is already taken. Be more creative than you are."
        except:
            pass
        if len(response_form.errors) > 0:
            for tag, error in response_form.errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')

        else:
            houses = {1:'Thunderbirds',2:'Horned Serpent',3:'Wampus',4:'Pukwedgie'}
            house = houses[randint(1,4)]
            User.objects.create(name=name, email=email, wand_desc=wand_desc, house=house, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
            messages.add_message(request, messages.INFO, 'Success. Now log in.')
            return redirect('/')

def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        
        try:
            user = User.objects.get(name=name)
        except:
            messages.add_message(request, messages.INFO, 'Name does not exist.')
            return redirect('/')

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['curr_user_id'] = user.id
        return redirect('/ilvermorny/{}'.format(request.session['curr_user_id']))

def logout(request):
    request.session.clear()
    return redirect('/')