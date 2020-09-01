from django.shortcuts import render, redirect
from compose.forms import PostForm
from common.models import Post, Tag
from cities_light.models import City

from django.utils.safestring import mark_safe
import json

def init(request):
    return redirect('compose:new')

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                city=request.user.profile.default_city,
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
    context = {
        'form': form,
        'tag_names': tag_names_json,
    }
    return render(request, 'compose/new.html', context=context)
