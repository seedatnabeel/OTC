# from django.http import  HttpResponse
# from django.shortcuts import render
# from .models import Symptoms
#
# def index(request):
#     all_symptoms = Symptoms.objects.all()
#     context = {'all_symptoms' : all_symptoms,}
#     return render(request, 'symptoms/index.html', context)
#
###################################################################

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Symptoms
from .forms import PostForm
# from django.utils import encoding
from unidecode import unidecode
import infermedica_api

infermedica_api.configure(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')

def index(request):
    api = infermedica_api.get_api()
    # all_symptoms = Symptoms.objects.all()
    # context = {'all_symptoms' : all_symptoms,}
    print(request.method)
    # print(request)
    if (request.method == "POST"):
        debug = request.POST.getlist('checks[]')
        print(len(debug))
        request = infermedica_api.Diagnosis(sex='female', age=35)

        for x in range(1, len(debug)):
            request.add_symptom(debug[x], 'present')

        request = api.diagnosis(request)

        for x in range(1, 3):
            print(request.conditions[x])
            # print(next((item for item in request if item["probability"] >= "0.10")))
        # print(request['question'])


        number_of_symptoms = len(debug)

        return HttpResponseRedirect('/')

    else:  # request.GET
        form = PostForm()

    context = {
        "form": form,
    }
    return render(request, "symptoms/post_form.html", context)


####################################################################



        # def request_page(request):
#     if (request.GET.get('mybtn')):
#         counter = 8
#         print counter
#     return render('symptoms/index.html')