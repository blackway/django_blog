# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from picture.models import Picture
from picture.forms import PictureForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, Http404

def index(request):
    pictures = Picture.objects.order_by('-created_at')
    carousels =Picture.objects.order_by('-created_at')[:3]
    total_count = len(pictures)
    return render_to_response('picture/index.html', {'pictures': pictures, 'total_count': total_count, 'carousels': carousels}, context_instance=RequestContext(request))

def new(request):
    form = PictureForm()
    variables = RequestContext(request, { 'form': form })
    return render_to_response('picture/new.html', variables)

def create(request):
    if request.method == 'POST':
        print("request.FILES : {0}".format(request.FILES))
        form = PictureForm(request.POST, request.FILES)
        print("form : {0}".format(form))

        if form.is_valid():
            # file is saved
            picture = Picture(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                file=request.FILES['file']
            )
            picture.save()
            return HttpResponseRedirect('/picture/')
        else:
            return render(request, 'picture/new.html', {'form': form})
    else:
        form = PictureForm()
    return render(request, 'picture/index.html', {'form': form})

def show(request, id):
    try:
        picture = Picture.objects.get(id=id)
        # board = get_object_or_404(Board, id=id)
    except:
        raise Http404('게시판을 찾을 수 없습니다.')
    form = PictureForm({'title':picture.title,
                        'description':picture.description,
                        'file':picture.file})

    variables = RequestContext(request, { 'form': form, 'id': id})
    return render_to_response('picture/show.html', variables)

def delete(request, id):
    try:
        print("#######################")
        picture = Picture.objects.get(id=id)
        picture.delete()
        # board = get_object_or_404(Board, id=id)
    except:
        raise Http404('삭제 할수 없습니다.')
    return HttpResponseRedirect('/picture')

