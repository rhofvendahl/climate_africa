from django.shortcuts import render

def init(request):
    context = {}
    return render(request, 'compose/compose.html', context=context)
