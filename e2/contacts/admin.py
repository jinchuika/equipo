from django.contrib import admin
from contacts.models import *

admin.site.register(Contact)
admin.site.register(Phone)
admin.site.register(DonationType)
admin.site.register(Donation)
admin.site.register(MeetingPurpose)
admin.site.register(Meeting)
admin.site.register(Account)
admin.site.register(Withdrawal)
admin.site.register(WithdrawalPurpose)