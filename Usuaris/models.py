# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuari (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to='../media/Perfils', default='../media/Perfils/Default.png', blank=True)
    monedes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username
