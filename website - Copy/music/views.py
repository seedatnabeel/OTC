from django.http import  HttpResponse
from django.shortcuts import render
from .models import Symptoms
from .forms import PostForm

def index(request):
    #all_symptoms = Symptoms.objects.all()
    #context = {'all_symptoms' : all_symptoms,}
    form=PostForm(request.POST or None)
    debug = request.POST.getlist('checks')
    print(debug)

    context = {
        "form":form,
    }
    return render(request, "music/post_form.html", context)

