from django import forms
from models import Person, Phone


class PersonForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    birthday = forms.DateField()

    class Meta:
        model = Person
        exclude = ()

    def __init__(self, *args, **kwargs):
        return super(PersonForm, self).__init__(*args, **kwargs)
        
class PhoneForm(forms.Form):
    number= forms.CharField(max_length=10)
    
    class Meta:
        model = Phone
        fields = ('number')
    
    def save(self, commit = True):
        Phone = super(PhoneForm, self).save(commit =False)
        Phone.number = self.cleaned_data['number']
    
        if commit:
            phone.save()        
        return phone