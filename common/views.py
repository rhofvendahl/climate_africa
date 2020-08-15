from django.shortcuts import render, redirect
# from common.models import Post

# def test(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'common/test.html', context=context)

def init(request):
    return redirect('browse:init')
