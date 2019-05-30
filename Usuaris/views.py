# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import *
from Usuaris.models import Usuari
from Publicacio.views import *
from django.contrib.auth import logout as d_logout

# Create your views here.
def registre(request):
    form = Registrar(request.POST, request.FILES)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    context = {'formulari': form}
    if request.method == 'POST':
        context = {'formulari': form, 'POST': True}
        print("errors")
        print(form.errors)
        if form.is_valid():
            nick = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            correu = form.cleaned_data.get('email')
            imatge = form.cleaned_data.get('imatge')
            form.save()
            name = request.POST['username']
            contrasenya = request.POST['password1']
            print(name)
            print(contrasenya)
            user = authenticate(username=name, password=contrasenya)
            login(request, user)
            Usuari.objects.create(user=request.user, imatge=imatge)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'Registre.html', context)


# def inici(request):
#     form = Login(request.POST, request.FILES)
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(reverse('index'))
#     context = {'formulari': form}
#     if request.method == 'POST':
#         context = {'formulari': form, 'POST': True}
#         print("errors")
#         print(form.errors)
#         if form.is_valid():
#             nick = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password2')
#             name = request.POST['username']
#             contrasenya = request.POST['password2']
#             user = authenticate(username=nick, password=password)
#             login(request, user)
#             return HttpResponseRedirect(reverse('index'))
#     return render(request, 'Inici_sessio.html', context)
#
#
# def logout(request):
#     if request.user.is_authenticated:
#         print("log out")
#         d_logout(request)
#     return HttpResponseRedirect(reverse('index'))
