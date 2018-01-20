# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'users':User.objects.all()
    }
    return render(request, 'users/index.html', context)

def newUser(request):
    return render(request, 'users/newUser.html')

def createUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        User.objects.create(first_name=first_name, last_name=last_name, email=email)

    return redirect('/users/' + str(User.objects.last().id))

def show(request, number):
    context = {
        'user':User.objects.get(id=number)
    }
    return render(request, 'users/user.html', context)

def edit(request, number):
    context = {
        'user':User.objects.get(id=number)
    }
    return render(request, 'users/editUser.html', context)

def update(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        print user.first_name
        print user.id
        user.save()
    
    return redirect('/users/' + str(user.id))

def destroy(request, number):
    user = User.objects.get(id=number)
    user.delete()
    return redirect('/users/')