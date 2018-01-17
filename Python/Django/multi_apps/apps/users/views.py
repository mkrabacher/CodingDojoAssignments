# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def login(request):
	return HttpResponse('placeholder for users to login')

def register(request):
	return HttpResponse('placeholder for users to create a new user record')

def users(request):
	return HttpResponse('placeholder to later display all the list of users')