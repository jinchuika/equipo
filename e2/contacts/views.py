from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from contacts.forms import PhoneForm, ContactForm, ContactModelForm
from contacts.models import Phone, Contact

def index(request):
	contact_list = Contact.objects.all().order_by('first_name')
	
	for contact in contact_list:
		contact_phones = Phone.objects.filter(contact=contact)
		contact.phone_data = [{
		'phone_number' : l.phone_number, 'description': l.description, 'empresa': l.empresa()
		}
		for l in contact_phones]
	return render(request, 'contacts/index.html', {'contact_list': contact_list})

def contact_detail(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	contact_phones = Phone.objects.filter(contact=contact)
	context = {
	'contact': contact,
	'contact_phones': contact_phones
	}

	return render(request, 'contacts/detail.html', context)

def create_contact(request, contact_id):
	contact = Contact.objects.get(id=contact_id)

	#Create the formest for the phone
	PhoneFormSet = formset_factory(PhoneForm)

	#get the existing data for this contact
	contact_phones = Phone.objects.filter(contact=contact)
	phone_data = [{
	'phone_number' : l.phone_number
	}
	for l in contact_phones]

	if request.method == 'POST':
		contact_form = ContactForm(request.POST, contact=contact)
		phone_formset = PhoneFormSet(request.POST)

		if contact_form.is_valid() and phone_formset.is_valid():
			#saves the contact info
			contact.first_name = contact_form.cleaned_data.get('first_name')
			contact.last_name = contact_form.cleaned_data.get('last_name')
			contact.birthday = contact_form.cleaned_data.get('birthday')
			contact.save()

			new_phones = []

			for phone_form in phone_formset:
				phone_number = phone_form.cleaned_data.get('phone_number')

				if phone_number:
					new_phones.append(Phone(contact=contact, phone_number=phone_number))

			try:
				with transaction.atomic():
					#replace the phone numbers
					Phone.objects.filter(contact=contact).delete()
					Phone.objects.bulk_create(new_phones)

					messages.success(request, 'Perfil actualizado')
			except IntegrityError:
				messages.error(request, 'Hubo un error')

	else:
		contact_form = ContactForm(contact=contact)
		phone_formset = PhoneFormSet(initial=phone_data)

	context = {
	'contact_form': contact_form,
	'phone_formset': phone_formset,
	}

	return render(request, 'contacts/contact_template.html', context)

def new_contact(request):
	if request.method=='POST':
		form = ContactModelForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.save()
			return redirect(create_contact, contact_id=contact.id)
	else:
		form = ContactModelForm()

	return render(request, 'contacts/new.html', {'form': form})