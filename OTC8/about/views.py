from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'about/index.html'
    response = HttpResponse("<h1>This is the Medications page")

    flu = 'http://otcsa.azurewebsites.net/list-of-illnesses/influenza-flu/'

    context = {
        "flu": flu
    }

    return render(request, template, context)

