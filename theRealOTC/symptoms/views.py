from django.http import  HttpResponse
from django.shortcuts import render
from .models import Symptoms

def index(request):
    all_symptoms = Symptoms.objects.all()
    context = {'all_symptoms' : all_symptoms,}
    return render(request, 'symptoms/index.html', context)