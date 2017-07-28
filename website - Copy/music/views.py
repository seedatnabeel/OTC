from django.http import  HttpResponse
from django.shortcuts import render
from .models import Symptoms
from .forms import PostForm
# from django.utils import encoding
from unidecode import unidecode

def index(request):
    #all_symptoms = Symptoms.objects.all()
    #context = {'all_symptoms' : all_symptoms,}
    print (request.method)
    # print(request)
    if(request.method == "POST"):
        debug = request.POST.getlist('checks')
        print(unidecode(debug[0]))
        return None

    else: #request.GET
        form = PostForm()

    context = {
        "form":form,
    }
    return render(request, "music/post_form.html", context)

