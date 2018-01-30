# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..users.models import *
from django.db.models import Count
from django.contrib import messages
from datetime import datetime
import time
from models import *
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def student(request, number):
    context = {
        'user':User.objects.get(id=request.session['curr_user_id']),
        'next_class':Class.objects.filter(start__gt=datetime.now().time())
    }
    return render(request, 'school/student.html', context)

def classes(request, number):
    class_rating = 0
    for rating in Rating.objects.filter(rated_class__id=number):
        class_rating += rating.score

    class_rating /= len(Rating.objects.filter(rated_class__id=number))

    context = {
        'class':Class.objects.get(id=number),
        'user':User.objects.get(id=request.session['curr_user_id']),
        'ratings':Rating.objects.all(),
        'class_rating':class_rating
    }


    return render(request, 'school/class.html', context)

def classesPage(request):
    context = {
        'classes':Class.objects.annotate(num_students=Count('students')).all(),
    }
    return render(request, 'school/classes.html', context)

def createClass(request):
    if request.method =='POST':
        user_id = request.session['curr_user_id']
        name = request.POST['name']
        desc = request.POST['desc']
        start = request.POST['start']
        end = request.POST['end']
        spots = request.POST['spots']
        teacher = User.objects.get(id=user_id)

        user_classes = Class.objects.filter(students__id=user_id)
        for class_ in user_classes:
            if timedelta(end, class_.start) > 0:
                messages.add_message(request, messages.INFO, "You don't have time to teach this")
                return redirect('/ilvermorny/classesPage')
            
        Class.objects.create(name=name, desc=desc, start=start, end=end, teacher=User.objects.get(id=user_id), spots=spots, total_spots=spots)

    class_id = Class.objects.last().id
    return redirect('/ilvermorny/classes/{}'.format(class_id))

def enrollClass(request):
    if request.method == "POST":
        student = User.objects.get(id=request.session['curr_user_id'])
        this_class = Class.objects.get(id=request.POST['id'])
        start = request.POST['start']
        end = request.POST['end']

        user_classes = Class.objects.filter(students__id=request.session['curr_user_id'])
        for class_ in user_classes:
            if end > class_.start and end < class_.end:
                messages.add_message(request, messages.INFO, "You don't have time to be in this class")
                return redirect('/ilvermorny/classes/' + request.POST['id'])

        student.classes.add(this_class)
        messages.add_message(request, messages.INFO, "Enrolled")
        return redirect('/ilvermorny/classes/' + request.POST['id'])


def cancelClass(request):
    if request.method == 'POST':
        class_id = request.POST['id']
        delClass = Class.object.get(id=class_id)
        delClass.delete()
    return redirect('ilvermorny/classes/')

def createRating(request):
    if request.method == "POST":
        score = request.POST['score']
        comment = request.POST['comment']
        class_ = Class.objects.get(id=request.POST['id'])
        rater = User.objects.get(id=request.session['curr_user_id'])

        if int(score) < 0 or int(score) > 5:
            messages.add_message(request, messages.INFO, "score must be between 0 and 5")
            return redirect('/ilvermorny/classes/' + str(class_.id))

        rating = Rating.objects.create(score=score, comment=comment, rated_class=class_, rater=rater)
        rater.save()    
        messages.add_message(request, messages.INFO, "rating submitted")
        return redirect('/ilvermorny/classes/' + str(class_.id))

def timeForm(request):
    return render(request,'school/timeForm.html')

def timeSubmit(request):
    if request.method == "POST":
        t1 = request.POST['time1']
        t2 = request.POST['time2']
        currentDT = datetime.now()

        print t1
        print t2
        # print currentDT
        # print datetime.now()
        
        print currentDT.strftime("%Y-%m-%d %H:%M:%S")
        print currentDT.strftime("%Y/%m/%d")
        print currentDT.strftime("%H:%M:%S")
        print currentDT.strftime("%I:%M %p")
        t3 = currentDT.strftime("%H:%M %p")
        print currentDT.strftime("%a, %b %d, %Y")

    context = {
        'output':t1 < t3,
        't1':t1,
        't2':t2,
        'currentDT':currentDT,
        'currentT':t3,
    }

    return render(request, 'school/timeForm.html', context)