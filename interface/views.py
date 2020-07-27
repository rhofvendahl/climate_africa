from django.shortcuts import render
from posts.models import Post

def test(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'interface/test.html', context=context)
