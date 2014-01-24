# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board)

"""
Board 테이블
제목
내용
생성일자
수정일자

"""