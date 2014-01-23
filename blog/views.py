# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from blog.models import Board
def main_page(request):
    boards = Board.objects.order_by('-created_at')[:10]
    variables = RequestContext(request, { 'boards': boards})
    return render_to_response('blog/main_page.html', variables)

def create(request):
    pass