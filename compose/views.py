from django.shortcuts import render, redirect
from compose.forms import PostForm
from common.models import Post, Tag, Image
from cities_light.models import City, Country

from django.utils.safestring import mark_safe
import json

def init(request):
    return redirect('compose:new')

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            city_name = json.loads(form.cleaned_data['city'])['text']
            city_object = City.objects.get(name=city_name)

            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                # image=form.cleaned_data.get('image'),
                city=city_object,
                type=form.cleaned_data.get('type'),
                event_date = form.cleaned_data.get('event_date'),
                well_amount = form.cleaned_data.get('well_amount'),
                well_population = form.cleaned_data.get('well_population')
            )

            image = Image.objects.create(
                post=post,
                order_in_post=1,
                image=form.cleaned_data.get('image'),
            )

            # tags = json.loads(form.cleaned_data['tags'])
            # for tag in tags:
            #     tag_object, created = Tag.objects.get_or_create(name=tag['text'])
            #     post.tags.add(tag_object)

            if form.cleaned_data['report_type']:
                report_type_dict = json.loads(form.cleaned_data['report_type'])
                report_type_filter = Tag.objects.filter(
                    name=report_type_dict['text'],
                    type='report_type',
                )
                if report_type_filter.exists():
                    report_type_tag = report_type_filter.first()
                else:
                    report_type_tag = Tag.objects.create(
                        name=report_type_dict['text'],
                        type='report_type',
                        is_starter=False,
                    )
                post.tags.add(report_type_tag)

            for report_impact_dict in json.loads(form.cleaned_data['report_impacts']):
                report_impact_filter = Tag.objects.filter(
                    name=report_impact_dict['text'],
                    type='report_impact',
                )
                if report_impact_filter.exists():
                    report_impact_tag = report_impact_filter.first()
                else:
                    report_impact_tag = Tag.objects.create(
                        name=report_impact_dict['text'],
                        type='report_impact',
                        is_starter=False,
                    )
                post.tags.add(report_impact_tag)

            for project_intention_dict in json.loads(form.cleaned_data['project_intentions']):
                project_intention_filter = Tag.objects.filter(
                    name=project_intention_dict['text'],
                    type='project_intention',
                )
                if project_intention_filter.exists():
                    project_intention_tag = project_intention_filter.first()
                else:
                    project_intention_tag = Tag.objects.create(
                        name=project_intention_dict['text'],
                        type='project_intention',
                        is_starter=False,
                    )
                post.tags.add(project_intention_tag)

            return redirect('common:init') # replace with animation page
    else:
        form = PostForm()
    # tag_names = [tag.name for tag in Tag.objects.all()]
    # tag_names_json = mark_safe(json.dumps(tag_names))

    country_city_names = [{
        'text': country.name,
        'children': [{
            'id': city.name + '; ' + country.name,
            'text': city.name,
        } for city in country.city_set.all()]
    } for country in Country.objects.filter(continent='AF')]
    country_city_names_json = mark_safe(json.dumps(country_city_names))

    report_type_names = [tag.name for tag in Tag.objects.filter(type='report_type', is_starter=True)]
    report_type_names_json = mark_safe(json.dumps(report_type_names))
    report_impact_names = [tag.name for tag in Tag.objects.filter(type='report_impact', is_starter=True)]
    report_impact_names_json = mark_safe(json.dumps(report_impact_names))
    project_intention_names = [tag.name for tag in Tag.objects.filter(type='project_intention', is_starter=True)]
    project_intention_names_json = mark_safe(json.dumps(project_intention_names))

    context = {
        'form': form,
        # 'tag_names': tag_names_json,
        'city_names': country_city_names_json,
        'report_type_names': report_type_names_json,
        'report_impact_names': report_impact_names_json,
        'project_intention_names': project_intention_names_json,
    }
    # print('COUNTRY CITY NAMES', country_city_names_json)
    return render(request, 'compose/new.html', context=context)
