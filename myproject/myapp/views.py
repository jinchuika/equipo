from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Person, Phone
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from forms import PhoneForm
import forms


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def person(request):
    return render(request, 'person.html', {
        'form': form_class,
    })
    
def member(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("No existe la persona")
    return render(request, 'person/member.html', {'person': person})

def detail(request, person_id):
    response = "Este es el detalle para el integrante %s."
    return HttpResponse(response % person_id)

def all_person(request):
    person_list = Person.objects.all()
    template = loader.get_template('person/index.html')
    context = {'person_list': person_list}
    return render(request, 'person/index.html', context)

def create_phone(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    try:
        phone = Phone(person=person, number='54645757')
    except Exception, e:
        raise e
    else:
        phone.save()

def new_phone(request):
    if request.method == 'POST':
        form =  PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('person/all.html')
    args = {}
    #args.update(csrf(request))
    args['form'] = PhoneForm()
    print args
    return render(request, 'person/phone_form.html', args)

class CreatePersonView(CreateView):
    model = Person
    template_name = 'person/edit_person.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('member')

class UpdatePersonView(UpdateView):
    model = Person
    template_name = 'person/edit_person.html'
    form_class = forms.PersonForm