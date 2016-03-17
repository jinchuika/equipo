from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from contacts.forms import *
from contacts.models import *
import datetime
from operator import attrgetter, methodcaller

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
	contact_donations = Donation.objects.filter(contact=contact)
	context = {
	'contact': contact,
	'contact_phones': contact_phones,
	'contact_donations': contact_donations,
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

def new_donation(request):
	if request.method=='POST':
		donation_form = DonationForm(request.POST)
		if donation_form.is_valid():
			donation = donation_form.save(commit=False)
			donation.save()
			return redirect(contact_detail, contact_id=donation.contact.id)
	else:
		donation_form = DonationForm()

	return render(request, 'donations/new.html', {'donation_form': donation_form})

def new_meeting(request):
	if request.method=='POST':
		meeting_form = MeetingForm(request.POST)
		if meeting_form.is_valid():
			meeting = meeting_form.save(commit=False)
			meeting.save()
			return redirect(index)
	else:
		meeting_form = MeetingForm(initial={'date':datetime.date.today})

	return render(request, 'meetings/new.html', {'meeting_form': meeting_form})

def meeting_index(request):
	meeting_list = Meeting.objects.all().order_by('date')
	return render(request, 'meetings/index.html', {'meeting_list': meeting_list})

def meeting_detail(request, meeting_id):
	meeting = Meeting.objects.get(id=meeting_id)
	return render(request, 'meetings/detail.html', {'meeting': meeting})

def meeting_edit(request, meeting_id):
	meeting = Meeting.objects.get(id=meeting_id)

	if request.method=='POST':
		meeting_form = MeetingEditForm(request.POST, meeting=meeting)
		if meeting_form.is_valid():
			meeting.date = meeting_form.cleaned_data.get('date')
			meeting.purpose = meeting_form.cleaned_data.get('purpose')
			meeting.participants = meeting_form.cleaned_data.get('participants')
			meeting.save()
			return redirect(meeting_index)
	else:
		meeting_form = MeetingEditForm(meeting=meeting)

	return render(request, 'meetings/edit.html', {'meeting_form': meeting_form})

def new_withdrawal(request):
	if request.method=='POST':
		withdrawal_form = WithdrawalForm(request.POST)
		if withdrawal_form.is_valid():
			withdrawal = withdrawal_form.save(commit=False)
			withdrawal.save()
			return redirect(index)
	else:
		withdrawal_form = WithdrawalForm()

	return render(request, 'withdrawals/new.html', {'form': withdrawal_form})

def money_index(request):
	movement_list = []
	donation_list = Donation.objects.all()
	withdrawal_list = Withdrawal.objects.all()
	for donation in donation_list:
		movement_list.append({'amount':donation.amount, 'date': donation.donation_date, 'type': 'donation'})

	for withdrawal in withdrawal_list:
		movement_list.append({'amount':withdrawal.amount, 'date': withdrawal.date, 'type': 'withdrawal'})

	return render(request, 'money/index.html', {'movement_list': sorted(movement_list, key=lambda k: k['date'])})