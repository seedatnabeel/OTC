from django.http import HttpResponse, Http404
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

    cause = infermedica_api.Diagnosis(sex='female', age=35)

    for x in range(0, len(debug)):
        cause.add_symptom(debug[x], 'present')

    cause = api.diagnosis(cause)

    first_cause=cause.conditions[0]['name']
    second_cause=cause.conditions[1]['name']
    third_cause=cause.conditions[2]['name']

    first_prob=cause.conditions[0]['probability']
    second_prob=cause.conditions[1]['probability']
    third_prob=cause.conditions[2]['probability']

    print(first_cause)
    print(first_prob*100)

##############################
    common_cold = 'http://otcsa.azurewebsites.net/list-of-illnesses/cold/'
    influenza = 'http://otcsa.azurewebsites.net/list-of-illnesses/influenza-flu/'
    acute_sinusitis = 'http://otcsa.azurewebsites.net/list-of-illnesses/sinusitis/'
    acid_reflux = 'http://otcsa.azurewebsites.net/list-of-illnesses/acid-reflux/'
    conjunctivitis = 'http://otcsa.azurewebsites.net/list-of-illnesses/conjunctivitis-pinkeye/'
  #  stomach_flu = 'http://otcsa.azurewebsites.net/list-of-illnesses/gastroenteritis-stomach-flu/'
    headache = 'http://otcsa.azurewebsites.net/list-of-illnesses/headache/'
    joint_pain = 'http://otcsa.azurewebsites.net/list-of-illnesses/joint-pain/'
    migraine = 'http://otcsa.azurewebsites.net/list-of-illnesses/migraine/'
  #  muscle_pain = 'http://otcsa.azurewebsites.net/list-of-illnesses/muscle-pain/'
    rhinitis_allergic = 'http://otcsa.azurewebsites.net/list-of-illnesses/rhinitis-allergic-hayfever/'
    med = '/treatment'



    if first_cause == "Common cold":
        first_cause1 = common_cold
    elif first_cause == "Influenza":
        first_cause1 = influenza
    elif first_cause == "Acute sinusitis":
        first_cause1 = acute_sinusitis
    elif first_cause == "Acid reflux disease":
        first_cause1 = acid_reflux
    elif first_cause == "Conjunctivitis":
        first_cause1 = conjunctivitis
 #   elif first_cause == "":
 #       first_cause1 = stomach_flu
    elif first_cause == "Tension-type headaches":
        first_cause1 = headache
    elif first_cause == "Joint or bone trauma":
        first_cause1 = joint_pain
    elif first_cause == "Migraine":
        first_cause1 = migraine
   # elif first_cause == "Muscle Pain":
   #     first_cause1 = muscle_pain
    elif first_cause == "Allergic rhinitis":
        first_cause1 = rhinitis_allergic
    else:
        first_cause1 = treatment

    if second_cause == "Common cold":
        second_cause1 = common_cold
    elif second_cause == "Influenza":
        second_cause1 = influenza
    elif second_cause == "Acute sinusitis":
        second_cause1 = acute_sinusitis
    elif first_cause == "Acid reflux disease":
        second_cause1 = acid_reflux
    elif second_cause == "Conjunctivitis":
        second_cause1 = conjunctivitis
    elif second_cause == "Tension-type headaches":
        second_cause1 = headache
    elif second_cause == "Joint or bone trauma":
        second_cause1 = joint_pain
    elif second_cause == "Migraine":
        second_cause1 = migraine
 #   elif second_cause == "Muscle Pain":
 #       second_cause1 = muscle_pain
    elif second_cause == "Allergic rhinitis":
        second_cause1 = rhinitis_allergic
    else:
        second_cause1 = treatment

    if third_cause == "Common cold":
        third_cause1 = common_cold
    elif third_cause == "Influenza":
        third_cause1 = influenza
    elif third_cause == "Acute sinusitis":
        third_cause1 = acute_sinusitis
    elif third_cause == "Acid reflux disease":
        third_cause1 = acid_reflux
    elif third_cause == "Conjunctivitis":
        third_cause1 = conjunctivitis
    elif third_cause == "Tension-type headaches":
        third_cause1 = headache
    elif third_cause == "Joint or bone trauma":
        third_cause1 = joint_pain
    elif third_cause == "Migraine":
        third_cause1 = migraine
 #   elif third_cause == "Muscle Pain":
 #       third_cause1 = muscle_pain
    elif third_cause == "Allergic rhinitis":
        third_cause1 = rhinitis_allergic
    else:
        third_cause1 = treatment

    context = {
        "first_cause": first_cause,
        "second_cause" : second_cause,
        "third_cause" : third_cause,
        "first_prob" : int(first_prob*100),
        "second_prob" : int(second_prob*100),
        "third_prob" : int(third_prob*100),
        "first_cause1": first_cause1,
        "second_cause1": second_cause1,
        "third_cause1": third_cause1
    }

    def index(request):

        print(request.method)
        if (request.method == "POST"):
            debug = request.POST.getlist('checks[]')
            request.session['name'] = debug

            return HttpResponseRedirect('/treatment/')


    return render(request, "causes/index.html", context)

