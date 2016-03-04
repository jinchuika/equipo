from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def person(request):
    return render(request, 'person.html', {
        'form': form_class,
    })
    
def member(request, person_id):
    return HttpResponse('Este es el integrante %s.', person_id)

def detail(request, person_id):
    response = "Este es el detalle para el integrante %s."
    return HttpResponse(response % person_id)

def all_person(request):
    person_list = Person.objects.all()
    template = loader.get_template('person/index.html')
    context = {
        'person_list': person_list
    }
    return HttpResponse(template.render(context, request))