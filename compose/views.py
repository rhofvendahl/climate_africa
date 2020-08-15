from django.shortcuts import render, redirect

def init(request):
    return redirect('compose:new')

def new(request):
    context = {
    }
    return render(request, 'compose/new.html', context=context)
