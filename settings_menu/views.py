from django.shortcuts import render

def init(request):
    context = {}
    return render(request, 'settings_menu/settings.html', context=context)
