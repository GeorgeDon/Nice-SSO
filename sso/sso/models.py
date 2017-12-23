# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

class t_user(models.Model):
    userName = models.CharField(max_length=32,unique=True)
    userAlias = models.CharField(max_length=64)
    pwd = models.CharField(max_length=128)
    userType = models.IntegerField(default=0)

class t_comment(models.Model):
    message = models.TextField()
    date = models.CharField(max_length=64)