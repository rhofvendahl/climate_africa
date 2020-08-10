from django.shortcuts import render
from common.models import Post

def test(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'common/test.html', context=context)
