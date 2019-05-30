# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Mitologia(models.Model):
    nom = models.CharField(max_length=100)
    origen = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nom


class Personatge(models.Model):
    nom = models.CharField(max_length=40)
    especie = models.CharField(max_length=40)
    imatge = models.ImageField(upload_to='../media/Imatges/', blank=False)
    poder_arma = models.CharField(max_length=200, blank=True)
    text = models.TextField(max_length=5000)
    altres_noms = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(default=timezone.now)
    id_mitologia = models.ForeignKey('Publicacio.Mitologia', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nom


class Test(models.Model):
    data = models.DateTimeField(default=timezone.now)
    actiu = models.BooleanField(default=False)
    id_personatge = models.ForeignKey('Publicacio.Personatge', on_delete=models.CASCADE, default=0)

    def __unicode__(self):
        return self.id_personatge.nom


class Preguntes(models.Model):
    pregunta = models.CharField(max_length=1500)
    resposta = models.CharField(max_length=150)
    opcio1 = models.CharField(max_length=150)
    opcio2 = models.CharField(max_length=150)
    opcio3 = models.CharField(max_length=150)
    id_test = models.ForeignKey('Publicacio.Test', on_delete=models.CASCADE, default=0)

    def __unicode__(self):
        return self.pregunta
