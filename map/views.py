from django.shortcuts import render, redirect

def init(request):
    return redirect('map:posts')

def posts(request):
    context = {
    }
    return render(request, 'map/posts.html', context=context)
