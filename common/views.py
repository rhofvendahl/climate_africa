from django.contrib import auth
from django.contrib.auth.models import User
from common.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from cities_light.models import City, Country
from django.utils.safestring import mark_safe
import json

from common.models import Profile, UserImage

def init(request):
    return redirect('browse:init')

def welcome(request):
    context = {

    }
    return render(request, 'common/welcome.html', context=context)

def join(request):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        if next is None:
            next = '/'

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )

                city_name = json.loads(form.cleaned_data['default_city'])['text']
                city_object = City.objects.get(name=city_name)
                profile = user.profile
                profile.default_city = city_object
                profile.is_organization = form.cleaned_data.get('is_organization')
                profile.bio = form.cleaned_data.get('bio')
                profile.website = form.cleaned_data.get('website')
                profile.email = form.cleaned_data.get('email')
                profile.name = form.cleaned_data.get('name')
                profile.save()

                if form.cleaned_data.get('user_image'):
                    image = UserImage.objects.create(
                        user=user,
                        image=form.cleaned_data.get('user_image')
                    )

                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect(next)
        else:
            form = CustomUserCreationForm()

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
            'next': next,
            'city_names': country_city_names_json,
        }
        return render(request, 'common/join.html', context=context)
    else:
        return redirect('/')

def login(request):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        if next is None:
            next = '/'

        if request.method == 'POST':
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect(next)
        else:
            form = CustomAuthenticationForm()
        context = {
            'form': form,
            'next': next,
        }
        return render(request, 'common/login.html', context=context)
    else:
        print('user is authenticated')
        return redirect('common:init')

def logout(request):
    auth.logout(request)
    return redirect('common:init')
