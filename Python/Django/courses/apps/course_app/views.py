# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect


def index(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'course_app/index.html', context)

def addCourse(request):
    if request.method == "POST":
        request.session['newCourse'] = {
            'name':request.POST['name'],
            'desc':request.POST['desc']
        }
    return redirect('/createCourse')

def createCourse(request):
    Course.objects.create(name=request.session['newCourse']['name'], desc=request.session['newCourse']['desc'])
    return redirect('/')

def remove(request, number):
    context = {
        'course':Course.objects.get(id=number)
    }
    return render(request, 'course_app/remove.html', context)

def removeCourse(request):

    course = Course.objects.get(id=request.POST['id'])
    course.delete()
    return redirect('/')