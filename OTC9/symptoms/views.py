from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Symptoms
from .forms import PostForm
# from django.utils import encoding
from unidecode import unidecode


def index(request):

    print(request.method)
    # print(request)
    if (request.method == "POST"):
        debug = request.POST.getlist('checks[]')

        request.session['name'] = debug

        return HttpResponseRedirect('/causes/')

    else:  # request.GET
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "symptoms/post_form.html", context)


def logo(request):
    log = 'symptoms/post_form.html'
    context = {
        "log" : log
    }
    return render(request, 'symptoms/post_form.html', context)