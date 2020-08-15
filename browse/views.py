from django.shortcuts import render, redirect
from common.models import Post

def init(request):
    return redirect('browse:posts')

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'browse/posts.html', context=context)
