from django.shortcuts import render, redirect
from common.models import Post, Support, UserImage, Tag
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from browse.forms import SearchForm
from django.utils.safestring import mark_safe
from django.contrib.postgres.search import SearchQuery, SearchVector
from cities_light.models import City, Country

import json

def init(request):
    return redirect('browse:posts')

def posts(request):
    showing_results = False
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            showing_results = True
            if form.cleaned_data['query']:
                query = SearchQuery(form.cleaned_data['query'])
                vector = SearchVector('title', 'text', 'user__profile__name')
                # this is where we'd adjust sort order, if that was supported
                posts = Post.objects.annotate(search=vector).filter(search=query)
            else:
                posts = Post.objects.all()

            if form.cleaned_data['type']:
                posts = posts.filter(type=form.cleaned_data['type'])

            if form.cleaned_data['city']:
                city_name = json.loads(form.cleaned_data['city'])['text']
                city_object = City.objects.get(name=city_name)
                posts = posts.filter(city=city_object)

            posts = posts.order_by('-created_at')

    else:
        form = SearchForm()
        posts = Post.objects.all().order_by('-created_at')

    # won't stand up to huge datasets; should eventually be done with fancy query
    available_country_city_names_dict = {}
    for post in Post.objects.all():
        city_name = post.city.name
        country_name = post.city.country.name
        if country_name in available_country_city_names_dict:
            if not city_name in available_country_city_names_dict[country_name]:
                available_country_city_names_dict[country_name].append(city_name)
        else:
            available_country_city_names_dict[country_name] = [city_name]

    available_country_city_names_list = [{
        'text': country_name,
        'children': [{
            'id': city_name + '; ' + country_name,
            'text': city_name,
        } for city_name in available_country_city_names_dict[country_name]]
    } for country_name in available_country_city_names_dict]
    available_country_city_names_json = mark_safe(json.dumps(available_country_city_names_list))

    context = {
        'posts': posts,
        'showing_results': showing_results,
        'form': form,
        'available_city_names': available_country_city_names_json,
    }
    for post in posts:
        print('IMAgE OBJECT', post.user.profile.user_image_or_none)
        if post.user.profile.user_image_or_none:
            print('IMAGE STUFF', post.user.profile.user_image_or_none.image)
            if post.user.profile.user_image_or_none.image:
                print('FILES STUFF', post.user.profile.user_image_or_none.image.url)
    return render(request, 'browse/posts.html', context=context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    # if post.first_image:
    #     f = open('testing.png', 'wb')
    #     f.write(post.first_image.image.read())
    #     f.close()

    # tag_names = [tag.name for tag in post.tags.all()]
    # tag_names_json = mark_safe(json.dumps(tag_names))

    report_type_tags = post.tags.filter(type='report_type')
    if report_type_tags.exists():
        report_type_tag_name = report_type_tags.first().name
    else:
        report_type_tag_name = None

    report_impact_tag_names = [tag.name for tag in post.tags.filter(type='report_impact')]
    report_impact_tag_names_json = mark_safe(json.dumps(report_impact_tag_names))

    project_intention_tag_names = [tag.name for tag in post.tags.filter(type='project-intention')]
    project_intention_tag_names_json = mark_safe(json.dumps(project_intention_tag_names))

    context = {
        'post': post,
        # 'tag_names': tag_names_json,
        'report_type': report_type_tag_name,
        'report_impact_tag_names': report_impact_tag_names_json,
        'project_intention_tag_names': project_intention_tag_names_json,
        'formatted_timestamp': post.created_at.strftime(f'%B {post.created_at.day}, %Y'),
        # 'supported': mark_safe(json.dumps(Support.objects.filter(supporter=request.user, supported_post=post).exists())),
        # 'support_url': mark_safe(json.dumps(reverse('browse:support_post', kwargs={'post_id': post.id}))),
        # 'unsupport_url': mark_safe(json.dumps(reverse('browse:unsupport_post', kwargs={'post_id': post.id}))),
    }
    return render(request, 'browse/post.html', context=context)

# @csrf_exempt
# def support_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     support, created = Support.objects.get_or_create(supporter=request.user, supported_post=post)
#     if created:
#         return JsonResponse({'message': 'Post supported.', 'supported': 'true', 'n_supporters': post.n_supporters}, status=200)
#     else:
#         return JsonResponse({'message': 'Error: Post already supported by user.', 'supported': 'true', 'n_supporters': post.n_supporters}, status=200)
#
# @csrf_exempt
# def unsupport_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     print(post.n_supporters)
#     supports = Support.objects.filter(supporter=request.user, supported_post=post)
#     if supports.count() == 0:
#         return JsonResponse({'message': 'Error: post not supported.', 'supported': 'false', 'n_supporters': post.n_supporters}, status=500)
#     elif supports.count() > 1:
#         supports.delete()
#         return JsonResponse({'message': 'Error: multiple supports exist for this post and user (all supports removed).', 'supported': 'false', 'n_supporters': post.n_supporters}, status=500)
#     else:
#         supports.delete()
#         return JsonResponse({'message': 'Support removed.', 'supported': 'false', 'n_supporters': post.n_supporters}, status=200)

def profile(request, user_id):
    # print('AAAAAAAAAAAAAAAAAAAAAAAAGGGGGGGGGG')
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'posts': user.post_set.all(),
        # 'supported': mark_safe(json.dumps(Support.objects.filter(supporter=request.user, supported_user=user).exists())),
        # 'support_url': mark_safe(json.dumps(reverse('browse:support_user', kwargs={'user_id': user.id}))),
        # 'unsupport_url': mark_safe(json.dumps(reverse('browse:unsupport_user', kwargs={'user_id': user.id}))),
    }
    # print('USER STUFF', user.post_set.all())
    return render(request, 'browse/profile.html', context=context)
    # return None
#
# @csrf_exempt
# def support_user(request, user_id):
#     user = User.objects.get(id=user_id)
#     support, created = Support.objects.get_or_create(supporter=request.user, supported_user=user)
#     if created:
#         return JsonResponse({'message': 'User supported.', 'supported': 'true', 'n_supporters': user.profile.n_supporters}, status=200)
#     else:
#         return JsonResponse({'message': 'Error: user already supported by current user.', 'n_supporters': user.profile.n_supporters}, status=500)
#
# @csrf_exempt
# def unsupport_user(request, user_id):
#     user = User.objects.get(id=user_id)
#     supports = Support.objects.filter(supporter=request.user, supported_user=user)
#     if supports.count() == 0:
#         return JsonResponse({'message': 'Error: user not supported.', 'supported': 'false', 'n_supporters': user.profile.n_supporters}, status=500)
#     elif supports.count() > 1:
#         supports.delete()
#         return JsonResponse({'message': 'Error: multiple supports exist for this current user and supported user (all supports removed).', 'supported': 'false', 'n_supporters': user.n_supporters}, status=500)
#     else:
#         supports.delete()
#         return JsonResponse({'message': 'Support removed.', 'supported': 'false', 'n_supporters': user.profile.n_supporters}, status=200)
