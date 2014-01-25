# -*- coding: utf-8 -*-
from django import forms

class PictureForm(forms.Form):
    title = forms.CharField(label='제목')
    description = forms.CharField(label='내용', required=False, widget=forms.Textarea(
        attrs={'cols':'80', 'rows':'6'}))
    file = forms.FileField(label='파일 선택')
