# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=27)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)