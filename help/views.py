from django.shortcuts import render, redirect

def init(request):
    return redirect('help:select')

def select(request):
    return render(request, 'help/select.html')
