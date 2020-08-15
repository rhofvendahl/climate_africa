from django.shortcuts import render

def init(request):
    context = {}
    return render(request, 'story/story.html', context=context)
