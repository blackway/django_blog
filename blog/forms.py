# -*- coding: utf-8 -*-
from argparse import RawDescriptionHelpFormatter
from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(label='제목')
    description = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'cols': '80', 'rows': '6'
    }))




    # title = models.CharField(max_length=200)
    # description = models.TextField(max_length=2000)
    # created_at = models.DateTimeField(auto_now_add=True)
    # board = models.ForeignKey(Board)