# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint
from time import gmtime, strftime
from django.shortcuts import render, redirect

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []

    
        
    return render(request, 'gold_app/index.html')

def process(request):
    if request.method == 'POST':
        loc = request.POST['location']
        if loc == 'farm':
            gold = randint(10,20)
            message = "you worked the fuck outta that field and got " + str(gold) + " from it. ("
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            request.session['log'].append(message + time + ')')
            request.session['log'] = request.session['log']
        elif loc == 'cave':
            gold = randint(5,10)
            message = "fell over in a cave, hit your head on a rock and found " + str(gold) + ". ("
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            request.session['log'].append(message + time + ')')
            request.session['log'] = request.session['log']
        elif loc == 'house':
            gold = randint(2,5)
            message = "you sat around the house all day and found " + str(gold) + " in a couch. ("
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            request.session['log'].append(message + time + ')')
            request.session['log'] = request.session['log']
        elif loc == 'casino':
            gold = randint(-50,50)
            if gold > 0:
                message = "you rolled them dice and WON " + str(gold) + " playa. ("
            elif gold == 0:
                message = "you rolled them dice and barely broke even. ("
            elif gold < 0:
                message = "you suck and gambling and lost " + str(gold) + " because you suck. ("
            time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            request.session['log'].append(message + time + ')')
            request.session['log'] = request.session['log']

        print 'gold:', gold
        request.session['gold'] += gold
        print 'message:', message 
        print 'time:', time 
        print 'request.session["log"]:', request.session['log'] 

        
        return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['log'] = []
    return redirect('/')