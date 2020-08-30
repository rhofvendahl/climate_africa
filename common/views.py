from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# from django.contrib.auth.forms import UserCreationForm
from common.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect

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
    next = request.GET.get('next')
    if next is None:
        next = '/'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            return redirect(next)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'next': next,
    }
    return render(request, 'common/join.html', context=context)

def login(request):
    next = request.GET.get('next')
    if next is None:
        next = '/'

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            return redirect(next)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'next': next,
    }
    return render(request, 'common/join.html', context=context)
