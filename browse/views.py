from django.shortcuts import render, redirect
from common.models import Post, Support
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from browse.forms import SearchForm
from django.utils.safestring import mark_safe
from django.contrib.postgres.search import SearchQuery, SearchVector

import json

def init(request):
    return redirect('browse:posts')

def posts(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print('QUERY', type(form.cleaned_data['query']))
            if form.cleaned_data['query']:
                query = SearchQuery(form.cleaned_data['query'])
                vector = SearchVector('title', 'text')
                posts = Post.objects.annotate(search=vector).filter(search=query)
            else:
                posts = Post.objects.all()
        else:
            pass
            # TODO: handle this
    else:
        form = SearchForm()
        posts = Post.objects.all()
    context = {
        'posts': posts,
        'form': form,
    }
    # for post in posts:
    #     print('IMAGE STUFF')
    #     print('1', post.first_image)
    #     if post.first_image:
    #         print('2', post.first_image.image)
    #         print('3', post.first_image.image.url)
    return render(request, 'browse/posts.html', context=context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.first_image:
        f = open('testing.png', 'wb')
        f.write(post.first_image.image.read())
        f.close()

    tag_names = [tag.name for tag in post.tags.all()]
    tag_names_json = mark_safe(json.dumps(tag_names))
    print('TAG NAMES', tag_names_json)
    context = {
        'post': post,
        'tag_names': tag_names_json,
        'formatted_timestamp': post.created_at.strftime(f'%B {post.created_at.day}, %Y'),
        'supported': mark_safe(json.dumps(Support.objects.filter(supporter=request.user, supported_post=post).exists())),
        'support_url': mark_safe(json.dumps(reverse('browse:support_post', kwargs={'post_id': post.id}))),
        'unsupport_url': mark_safe(json.dumps(reverse('browse:unsupport_post', kwargs={'post_id': post.id}))),
    }
    return render(request, 'browse/post.html', context=context)

@csrf_exempt
def support_post(request, post_id):
    post = Post.objects.get(id=post_id)
    support, created = Support.objects.get_or_create(supporter=request.user, supported_post=post)
    if created:
        return JsonResponse({'message': 'Post supported.', 'supported': 'true', 'n_supporters': post.n_supporters}, status=200)
    else:
        return JsonResponse({'message': 'Error: Post already supported by user.', 'supported': 'true', 'n_supporters': post.n_supporters}, status=200)

@csrf_exempt
def unsupport_post(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post.n_supporters)
    supports = Support.objects.filter(supporter=request.user, supported_post=post)
    if supports.count() == 0:
        return JsonResponse({'message': 'Error: post not supported.', 'supported': 'false', 'n_supporters': post.n_supporters}, status=500)
    elif supports.count() > 1:
        supports.delete()
        return JsonResponse({'message': 'Error: multiple supports exist for this post and user (all supports removed).', 'supported': 'false', 'n_supporters': post.n_supporters}, status=500)
    else:
        supports.delete()
        return JsonResponse({'message': 'Support removed.', 'supported': 'false', 'n_supporters': post.n_supporters}, status=200)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'posts': user.post_set.all(),
        'supported': Support.objects.filter(supporter=request.user, supported_user=user).exists(),
        'support_url': reverse('browse:support_user', kwargs={'user_id': user.id}),
        'unsupport_url': reverse('browse:unsupport_user', kwargs={'user_id': user.id}),
    }
    print('USER STUFF', user.post_set.all())
    return render(request, 'browse/profile.html', context=context)

@csrf_exempt
def support_user(request, user_id):
    user = User.objects.get(id=user_id)
    support, created = Support.objects.get_or_create(supporter=request.user, supported_user=user)
    if created:
        return JsonResponse({'message': 'User supported.', 'supported': 'true', 'n_supporters': user.n_supporters}, status=200)
    else:
        return JsonResponse({'message': 'Error: user already supported by current user.', 'n_supporters': user.n_supporters}, status=500)

@csrf_exempt
def unsupport_user(request, user_id):
    user = User.objects.get(id=user_id)
    supports = Support.objects.filter(supporter=request.user, supported_user=user)
    if supports.count() == 0:
        return JsonResponse({'message': 'Error: user not supported.', 'supported': 'false', 'n_supporters': user.n_supporters}, status=500)
    elif supports.count() > 1:
        supports.delete()
        return JsonResponse({'message': 'Error: multiple supports exist for this current user and supported user (all supports removed).', 'supported': 'false', 'n_supporters': user.n_supporters}, status=500)
    else:
        supports.delete()
        return JsonResponse({'message': 'Support removed.', 'supported': 'false', 'n_supporters': user.n_supporters}, status=200)
