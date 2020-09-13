from django.shortcuts import render, redirect
from compose.forms import PostForm
from common.models import Post, Tag
from cities_light.models import City, Country

from django.utils.safestring import mark_safe
import json

def init(request):
    return redirect('compose:new')

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            city_name = json.loads(form.cleaned_data['city'])['text']
            city_object = City.objects.get(name=city_name)
            print('CITYYYYY', city_object.id)

            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                city=city_object,
            )

            tags = json.loads(form.cleaned_data['tags'])
            for tag in tags:
                tag_object, created = Tag.objects.get_or_create(name=tag['text'])
                post.tags.add(tag_object)
            return redirect('common:init') # replace with animation page
    else:
        form = PostForm()
    tag_names = [tag.name for tag in Tag.objects.all()]
    tag_names_json = mark_safe(json.dumps(tag_names))

    country_city_names = [{
        'text': country.name,
        'children': [{
            'id': city.name + '; ' + country.name,
            'text': city.name,
        } for city in country.city_set.all()]
    } for country in Country.objects.filter(continent='AF')]
    country_city_names_json = mark_safe(json.dumps(country_city_names))

    context = {
        'form': form,
        'tag_names': tag_names_json,
        'city_names': country_city_names_json,
    }
    print('COUNTRY CITY NAMES', country_city_names_json)
    return render(request, 'compose/new.html', context=context)
