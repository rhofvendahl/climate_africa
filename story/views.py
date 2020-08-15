from django.shortcuts import render, redirect

def init(request):
    return redirect('story:stories')

def stories(request):
    context = {
    }
    return render(request, 'story/stories.html', context=context)
