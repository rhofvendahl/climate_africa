from django.shortcuts import render, redirect
from menu.forms import ChangeInfoForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import auth
from django.contrib.auth.models import User
from cities_light.models import City, Country
from django.utils.safestring import mark_safe
import json
from common.models import Profile, UserImage

def init(request):
    return redirect('menu:select')

def select(request):
    context = {
    }
    return render(request, 'menu/select.html', context=context)

def change_info(request):
    print('SITEEEE', request.user.profile.website, type(request.user.profile.website))
    if request.method == 'POST':
        form = ChangeInfoForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data.get('new_username')
            user.save()

            new_city_name = json.loads(form.cleaned_data['new_default_city'])['text']
            new_city_object = City.objects.get(name=new_city_name)
            profile = user.profile
            profile.default_city = new_city_object
            profile.name = form.cleaned_data.get('new_name')
            profile.email = form.cleaned_data.get('new_email')
            profile.bio = form.cleaned_data.get('new_bio')
            profile.website = form.cleaned_data.get('new_website')
            profile.save()

            # TODO something funk abt websites
            # TODO allow an option to remove image entirely
            new_image = form.cleaned_data.get('new_user_image')
            if new_image:
                image_object = UserImage.objects.get_or_create(user=user)
                image_object.image = form.cleaned_data.get('new_user_image')
                image_object.save()

            # image = UserImage.objects.create(
            #     user=user,
            #     image=form.cleaned_data.get('user_image')
            # )

            return redirect('menu:select')
    else:
        form = ChangeInfoForm(user=request.user)

    country_city_names = [{
        'text': country.name,
        'children': [{
            'id': city.name + '; ' + country.name,
            'text': city.name,
        } for city in country.city_set.all()]
    } for country in Country.objects.filter(continent='AF')]
    country_city_names_json = mark_safe(json.dumps(country_city_names))

    profile = request.user.profile
    old_info = {
        'username': request.user.username,
        'name': profile.name,
        'email': profile.email if profile.email else '',
        'bio': profile.bio if profile.bio else '',
        'default_city_id': profile.default_city.name + '; ' + profile.default_city.country.name,
        'user_image_url': profile.user_image_or_none.image.url if profile.user_image_or_none else '',
        'website': profile.website if profile.website else '',
    }
    old_info_json = mark_safe(json.dumps(old_info))
    context = {
        'form': form,
        'city_names': country_city_names_json,
        'old_info': old_info_json,
    }
    return render(request, 'menu/change_info.html', context=context)

def change_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('menu:select')
    else:
        form = SetPasswordForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'menu/change_password.html', context=context)
