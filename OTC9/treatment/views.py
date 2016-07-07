from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template = 'treatment/index.html'

    return render(request, template)

def inf(request):
    temp = 'treatment/influenza.html'
    return render(request, temp)

def ar(request):
    temp = 'treatment/acidreflux.html'
    return render(request, temp)
