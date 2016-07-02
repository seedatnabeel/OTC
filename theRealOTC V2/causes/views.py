from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'causes/index.html'
    response = HttpResponse("<h1>This is the causes page")
    return render(request, template)

