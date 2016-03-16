# -*- encoding: utf-8 -*-
from django.test import TestCase
from .models import Person

class PersonClass(TestCase):
	"""Person model"""
	def test_str(self):
		person = Person(first_name='Pedro', last_name='Roca')
		self.assertEquals(str(person), 'Pedro Roca')
		