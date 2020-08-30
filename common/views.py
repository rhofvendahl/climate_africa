# from django.contrib.auth import authenticate
# from django.contrib.auth import login as auth_login
from django.contrib import auth
# from django.contrib.auth.forms import AuthenticationForm
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
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        if next is None:
            next = '/'

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            print('DATATATATATA')
            print(form)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)

                return redirect(next)
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form,
            'next': next,
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
            print('FOOOOOOOOOOOOOOORM')
            print(form.data)
            print('REQUEEEEEEEST')
            print(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect(next)
                print('at least it got here')
            print('issue', form.errors, 'ugh')
        else:
            form = CustomAuthenticationForm()
            print('not post')
        context = {
            'form': form,
            'next': next,
        }
        print('something odds going on')
        return render(request, 'common/login.html', context=context)
    else:
        print('user is authenticated')
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')
