from django.http import HttpResponse
from django.shortcuts import render
import infermedica_api
from django.http import HttpResponseRedirect


infermedica_api.configure(app_id='945555e1', app_key='be2ee424c225c567086a084637a359de')

def index(request):
    api = infermedica_api.get_api()
    template = 'causes/index.html'
    response = HttpResponse("<h1>This is the causes page")
    debug = request.session['name']
    print(request.session['name'])
    print("we have this many:", len(debug))

    request = infermedica_api.Diagnosis(sex='female', age=35)

    for x in range(1, len(debug)):
        request.add_symptom(debug[x], 'present')

    request = api.diagnosis(request)



    first_cause=request.conditions[0]['name']
    second_cause=request.conditions[1]['name']
    third_cause=request.conditions[2]['name']

    first_prob=request.conditions[0]['probability']
    second_prob=request.conditions[1]['probability']
    third_prob=request.conditions[2]['probability']

    print(first_cause)
    print(first_prob*100)

    return render(request, "causes/index.html", context)

