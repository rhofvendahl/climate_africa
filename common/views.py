# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login
from django.contrib import auth
# from django.contrib.auth.forms import AuthenticationForm
from common.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from cities_light.models import City, Country
from django.utils.safestring import mark_safe
import json

# from common.models import Post

# def test(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'common/test.html', context=context)

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
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
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
        return redirect('common:init') # used to be '/'

def logout(request):
    auth.logout(request)
    return redirect('common:init')
