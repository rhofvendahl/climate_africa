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
    return render(request, 'browse/posts.html', context=context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)

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
        'report_type': report_type_tag_name,
        'report_impact_tag_names': report_impact_tag_names_json,
        'project_intention_tag_names': project_intention_tag_names_json,
        'formatted_timestamp': post.created_at.strftime(f'%B {post.created_at.day}, %Y'),
    }
    return render(request, 'browse/post.html', context=context)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user,
        'posts': user.post_set.all(),
    }
    return render(request, 'browse/profile.html', context=context)
