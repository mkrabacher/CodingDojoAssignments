from __future__ import unicode_literals
from django.db import models
from .models import User
from django import forms
from datetime import *

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=255, min_length=4)
    email = forms.EmailField()
    wand_desc = forms.CharField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)