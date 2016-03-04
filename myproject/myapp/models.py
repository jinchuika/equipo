from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    
class Phone(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)