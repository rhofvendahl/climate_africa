from django.shortcuts import render

def init(request):
    context = {}
    return render(request, 'map/map.html', context=context)
