from django.db import models

class Link(models.Model):
    link = models.CharField(max_length=100)
