"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import articles, pictures, comments
from .forms import PictureForm, CommentForm

def redir(request):
    assert isinstance(request, HttpRequest)
    return redirect('news')

def news(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/index.html',
        {
            'title':'Новости сайта',
            'newslist':articles.objects.all(),
            'year':datetime.now().year,
        }
    )
    
def article(request, n):
    artcl = articles.objects.get(id = n)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/article.html',
        {
            'title':artcl,
            'year':datetime.now().year,
        }
    )
    
def arts(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/arts.html',
        {
            'title':'Арты',
            'artslist':pictures.objects.all(),
            'year':datetime.now().year,
        }
    )
    
def art(request, n):
    artn = pictures.objects.get(id = n)
    comms = comments.objects.filter(post = n)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commf = form.save(commit = False)
            commf.author = request.user
            commf.date = datetime.now()
            commf.post = pictures.objects.get(id = n)
            commf.save()
            return redirect('art', n = artn.id)
    else:
        form = CommentForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/art.html',
        {
            'title':artn,
            'comms':comms,
            'form':form,
            'year':datetime.now().year,
        }
    )
    
def newart(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            blogf = form.save(commit = False)
            blogf.date = datetime.now()
            blogf.author = request.user
            blogf.save()
            return redirect('arts')
    else:
        form = PictureForm()
    assert isinstance(request, HttpRequest)
    return render(
        request, 'news/newart.html',
        {
            'title':'Добавить арт',
            'form':form,
            'year':datetime.now().year,
        }
    )