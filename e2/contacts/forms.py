from django import forms
from django.forms import ModelForm
from contacts.models import Contact, Donation, Meeting, MeetingPurpose
import datetime

class PhoneForm(forms.Form):
    phone_number = forms.IntegerField()

class ContactForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.contact = kwargs.pop('contact')
		super(ContactForm, self).__init__(*args, **kwargs)

		self.fields['first_name'] = forms.CharField(
			max_length=100,
			initial=self.contact.first_name)
		self.fields['last_name'] = forms.CharField(
			max_length=100,
			initial=self.contact.last_name)

class ContactModelForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['first_name', 'last_name']
		labels = {
		'first_name': 'Nombre',
		'last_name': 'Apellido'
		}

class DonationForm(ModelForm):
	class Meta:
		model = Donation
		fields = '__all__'
		labels = {
		'amount': 'Cantidad',
		'date': 'Fecha',
		'contact': 'Persona',
		'donation_type': 'Donado para'
		}

class MeetingForm(ModelForm):
	"""Form for managing meetings"""
	date = forms.DateField(initial=datetime.date.today, label='Fecha')
	purpose = forms.ModelChoiceField(queryset=MeetingPurpose.objects.all(), label='Propósito')
	participants = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple(),
		queryset=Contact.objects.all(),
		label='Asistentes')
	class Meta:
		model = Meeting
		fields = ('date', 'purpose', 'participants')
		labels= {
		'date': 'Fecha',
		'purpose': 'Propósito',
		'participants': 'Asistentes'
		}

class MeetingEditForm(forms.Form):
	def __init__(self, *args, **kwargs):
		self.meeting = kwargs.pop('meeting')
		super(MeetingEditForm, self).__init__(*args, **kwargs)

		self.fields['date'] = forms.DateField(
			initial=self.meeting.date,
			label='Fecha')
		self.fields['purpose'] = forms.ModelChoiceField(
			initial=self.meeting.purpose,
			queryset=MeetingPurpose.objects.all(),
			label='Propósito')
		self.fields['participants'] = forms.ModelMultipleChoiceField(
			initial=self.meeting.participants.all,
			widget=forms.CheckboxSelectMultiple(),
			queryset=Contact.objects.all(),
			label='Asistentes')