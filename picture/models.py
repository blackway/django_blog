# -*- coding: utf-8 -*-
from django.contrib.admin import widgets
from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    file = models.FileField(upload_to='static/upload_files/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
