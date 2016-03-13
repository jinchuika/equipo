from django.contrib import admin
from contacts.models import Contact, Phone, DonationType, Donation, MeetingPurpose, Meeting

admin.site.register(Contact)
admin.site.register(Phone)
admin.site.register(DonationType)
admin.site.register(Donation)
admin.site.register(MeetingPurpose)
admin.site.register(Meeting)