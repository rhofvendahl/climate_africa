from django.shortcuts import render, redirect
from common.models import Post
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
import json

def init(request):
    return redirect('browse:posts')

def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'browse/posts.html', context=context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    tag_names = [tag.name for tag in post.tags.all()]
    tag_names_json = mark_safe(json.dumps(tag_names))
    context = {
        'post': post,
        'tag_names': tag_names_json,
        'formatted_timestamp': post.created_at.strftime(f'%B {post.created_at.day}, %Y')
    }
    return render(request, 'browse/post.html', context=context)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'posts': user.post_set.all(),
    }
    print('USER STUFF', user.post_set.all())
    return render(request, 'browse/profile.html', context=context)
