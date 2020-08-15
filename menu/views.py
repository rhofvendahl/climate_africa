from django.shortcuts import render, redirect

def init(request):
    return redirect('menu:select')

def select(request):
    context = {
    }
    return render(request, 'menu/select.html', context=context)
