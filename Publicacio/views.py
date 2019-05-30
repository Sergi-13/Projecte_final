# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from Usuaris.models import Usuari
from Publicacio.models import Personatge
from Publicacio.models import Preguntes
from Publicacio.models import Test

import json


# Create your views here.
def index(request):
    personatges = Personatge.objects.order_by('data')[2]
    # if request.user.is_authenticated():
    #     context = {'personatges': personatges, 'username': request.user.username}
    # else:-
    context = {'personatges': personatges}
    return render(request, 'Index.html', context)


@login_required()
def test(request):
    personatge = Personatge.objects.order_by('data')[2]
    nom = personatge.nom
    id = personatge.pk
    print(nom)
    print(id)
    preguntes = Preguntes.objects.filter(id_test=id)
    context = {'preguntes': preguntes}
    return render(request, 'Test.html', context)


def personatge(request, personatge_id):
    personatge = Personatge.objects.get(pk=personatge_id)
    context = {'personatge': personatge}
    return render(request, 'Personatge.html', context)


def publicacions(request):
    personatges = Personatge.objects.order_by('-data')
    context = {'personatges': personatges}
    return render(request, 'Publicacions.html', context)


def cerca(request):
    if request.method == "GET":
        text = request.GET.get('criteri')
        llista = Personatge.objects.filter(nom__icontains=text)
        print(llista)
        sortida = [estructura(cerca) for cerca in llista]
        return HttpResponse(json.dumps(sortida), content_type='aplication/json')
    HttpResponseRedirect(reverse('index'))


def estructura(llista):
    print llista
    return {'id': llista.id, 'nom': llista.nom, 'imatge': llista.imatge.url}
