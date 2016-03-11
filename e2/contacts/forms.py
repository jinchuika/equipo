from django import forms
from django.forms import ModelForm
from contacts.models import Contact

class PhoneForm(forms.Form):
    phone_number = forms.IntegerField(
                    )

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