# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Usuaris.models import Usuari

class Registrar(UserCreationForm):
    imatge = forms.ImageField(required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class Login(User):
    username = forms.CharField(max_length=100, required=True)
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
