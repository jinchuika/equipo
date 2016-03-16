from django.contrib import admin

from myapp.models import Person
from myapp.models import Phone
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Phone)