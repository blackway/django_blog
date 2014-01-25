# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from blog.models import Board
from blog.forms import BoardForm
from django.http.response import HttpResponseRedirect, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404

def show(request, id):
    try:
        board = Board.objects.get(id=id)
        # board = get_object_or_404(Board, id=id)
    except:
        raise Http404('게시판을 찾을 수 없습니다.')
    form = BoardForm({'title':board.title, 'description':board.description})

    variables = RequestContext(request, { 'form': form})
    return render_to_response('blog/show.html', variables)

def index(request):
    # boards = Board.objects.order_by('-created_at')[:10]
    boards = Board.objects.order_by('-created_at')
    total_count = len(boards)

    # boards = Board.objects.raw('select * from blog_board')


    # boards = Board.objects.raw('select rowid as row_id, title,description from blog_board order by created_at desc ')
    return render_to_response('blog/index.html', {'boards': boards,
                                                  'total_count': total_count},
                              context_instance=RequestContext(request))
    # paginator = Paginator(boards, 5)
    # try:
    #     page = int(request.GET.get('page','1'))
    # except ValueError:
    #     page = 1
    # try:
    #     fp = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     fp = paginator.page(paginator.num_pages)
    #
    # variables = RequestContext(request, { 'mydata': fp})
    # return render_to_response('blog/main_page.html', variables)
    # return render_to_response('blog/main_page.html', {'mydata': fp})

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board, dummy = Board.objects.get_or_create(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description']
            )
            # board = Board(
            #     title = form.cleaned_data['title'],
            #     description = form.cleaned_data['description']
            # )
            board.save()
            return HttpResponseRedirect('/')
    else:
        form = BoardForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('blog/new.html', variables)


def new(request):
    # board = Board.objects.create()
    # variables = RequestContext(request, { 'board': board })
    form = BoardForm()
    variables = RequestContext(request, { 'form': form })
    return render_to_response('blog/new.html', variables)
