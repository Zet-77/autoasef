from django.shortcuts import get_object_or_404, render, redirect

#from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    return render(request, template) 


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
    

def post_detail(request, pk = 2):
    id = pk
    template = 'posts/post_detail.html'
    return render(request, id, template)


def auto(request):
    template = 'posts/auto.html'
    return render(request, template)


def moto(request):
    template = 'posts/moto.html'
    return render(request, template)    


def ja_auction(request):
    template = 'posts/ja_auction.html'
    return render(request, template)


def georgia(request):
    template = 'posts/georgia.html'
    return render(request, template)

# Create your views here.
