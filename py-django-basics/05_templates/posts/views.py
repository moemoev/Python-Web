from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

from datetime import datetime

from posts.models import Post


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()

    context = {
        'variable': 5,
        'user':{
            'name':'dimo',
            'age': 666,
        },
        'post': {
            'title': 'THIS IS A TEST POST',
            'content': 'Some description',
            'author': 'Dimo',
            'created_at': datetime.now(),
            'empyt': None,
            'markdown_context': ' **Some description** <i>inside</i> this',
        },
        'posts': posts,
    }
    return render(request, 'base.html', context)

def dashboard(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is THE Dashboard!!!\n Showcasing the URL - Tag")

def dashboard_pk(request: HttpRequest, pk=int) -> HttpResponse:
    return HttpResponse("This is THE Dashboard!!!\n Showcasing the URL - Tag")

def dashboard_custom_tags(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'custom_tags.html', context)