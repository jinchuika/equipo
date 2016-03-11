from django.contrib import admin
from contacts.models import Contact, Phone

admin.site.register(Contact)
admin.site.register(Phone)