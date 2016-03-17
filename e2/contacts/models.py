from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	birthday = models.DateField(null=True, blank=True)

	def __str__(self):
		return ' '.join([self.first_name, self. last_name])

class Phone(models.Model):
	phone_number = models.IntegerField(blank=True)
	description = models.CharField(max_length=50, null=True, blank=True)
	contact = models.ForeignKey('Contact', on_delete=models.CASCADE)

	def empresa(self):
	    if(self.phone_number < 30000000 or self.phone_number >= 60000000):
	        return "otro"

	    if (((30000000<= self.phone_number) and (self.phone_number <= 33599999)) or ((40000000<= self.phone_number) and (self.phone_number <= 40999999)) or ((44760000<= self.phone_number) and (self.phone_number <= 46999999)) or ((47730000<= self.phone_number) and (self.phone_number <= 48199999)) or ((48220000<= self.phone_number) and (self.phone_number <= 50099999)) or ((50300000<= self.phone_number) and (self.phone_number <= 50699999)) or ((51500000<= self.phone_number) and (self.phone_number <= 52099999)) or ((53000000<= self.phone_number) and (self.phone_number <= 53099999)) or ((53140000<= self.phone_number) and (self.phone_number <= 53899999)) or ((55200000<= self.phone_number) and (self.phone_number <= 55299999)) or ((55500000<= self.phone_number) and (self.phone_number <= 55539999)) or ((55800000<= self.phone_number) and (self.phone_number <= 55819999)) or ((57000000<= self.phone_number) and (self.phone_number <= 57099999)) or ((57190000<= self.phone_number) and (self.phone_number <= 57899999)) or ((58000000<= self.phone_number) and (self.phone_number <= 58099999)) or ((58190000<= self.phone_number) and (self.phone_number <= 58199999)) or ((58800000<= self.phone_number) and (self.phone_number <= 59099999)) or ((59180000<= self.phone_number) and (self.phone_number <= 59199999)) or ((59900000<= self.phone_number) and (self.phone_number <= 59999999))):
	        return "tigo"

	    elif (((34000000<= self.phone_number) and (self.phone_number <=34699999)) or ((43000000<= self.phone_number) and (self.phone_number <=44759999)) or ((50200000<= self.phone_number) and (self.phone_number <=50299999)) or ((50700000<= self.phone_number) and (self.phone_number <=51099999)) or ((51400000<= self.phone_number) and (self.phone_number <=51499999)) or ((52100000<= self.phone_number) and (self.phone_number <=52999999)) or ((53120000<= self.phone_number) and (self.phone_number <=53139999)) or ((53900000<= self.phone_number) and (self.phone_number <=54099999)) or ((55000000<= self.phone_number) and (self.phone_number <=55099999)) or ((55180000<= self.phone_number) and (self.phone_number <=55199999)) or ((55400000<= self.phone_number) and (self.phone_number <=55429999)) or ((55450000<= self.phone_number) and (self.phone_number <=55499999)) or ((56000000<= self.phone_number) and (self.phone_number <=56099999)) or ((56400000<= self.phone_number) and (self.phone_number <=56899999)) or ((57900000<= self.phone_number) and (self.phone_number <=57999999)) or ((59150000<= self.phone_number) and (self.phone_number <=59179999)) ):
	        return "movistar"

	    elif(((41000000<= self.phone_number) and (self.phone_number <=42999999)) or ((47000000<= self.phone_number) and (self.phone_number <=47729999)) or ((50100000<= self.phone_number) and (self.phone_number <=50199999)) or ((51100000<= self.phone_number) and (self.phone_number <=51399999)) or ((53100000<= self.phone_number) and (self.phone_number <=53119999)) or ((54100000<= self.phone_number) and (self.phone_number <=54999999)) or ((55100000<= self.phone_number) and (self.phone_number <=55179999)) or ((55300000<= self.phone_number) and (self.phone_number <=55399999)) or ((55430000<= self.phone_number) and (self.phone_number <=55449999)) or ((55540000<= self.phone_number) and (self.phone_number <=55799999)) or ((55820000<= self.phone_number) and (self.phone_number <=55999999)) or ((56100000<= self.phone_number) and (self.phone_number <=56399999)) or ((56900000<= self.phone_number) and (self.phone_number <=56999999)) or ((57100000<= self.phone_number) and (self.phone_number <=57189999)) or ((58100000<= self.phone_number) and (self.phone_number <=58189999)) or ((58200000<= self.phone_number) and (self.phone_number <=58799999)) or ((59100000<= self.phone_number) and (self.phone_number <=59149999)) or ((59200000<= self.phone_number) and (self.phone_number <=59899999))):
	        return "claro"

	    else:
	        return "otro"

	def __str__(self):
		return self.phone_number


class DonationType(models.Model):
	"""Type of donation"""
	donation_type = models.CharField(max_length=50)

	def __str__(self):
		return self.donation_type

class Donation(models.Model):
	"""Model for donations and givings"""
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	donation_date = models.DateField(null=True, blank=True)
	contact = models.ForeignKey('Contact', on_delete=models.SET_NULL, null=True, blank=True)
	donation_type = models.ForeignKey('DonationType', on_delete=models.SET_NULL, null=True, blank=True)
	account = models.ForeignKey('Account', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return "Q. " + str(self.amount) + " de " + str(self.contact)

@receiver(post_save, sender=Donation, dispatch_uid="update_accout_credit")
def update_credit_donation(sender, instance, **kwargs):
	instance.account.credit += instance.amount
	instance.account.save()

class MeetingPurpose(models.Model):
	"""Model for the type of meetings"""
	purpose = models.CharField(max_length=50)

	def __str__(self):
		return self.purpose
		
class Meeting(models.Model):
	"""Model for meetings and gatherings"""
	date = models.DateField()
	purpose = models.ForeignKey('MeetingPurpose', on_delete=models.SET_NULL, null=True, blank=True)
	participants = models.ManyToManyField(Contact, blank=True)

	def __str__(self):
		return str(self.date) + " (" + str(self.purpose) + ")"

class Account(models.Model):
	"""Model for the money accounts"""
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=150)
	credit = models.DecimalField(max_digits=10, decimal_places=2)

	
	def sum_total_transfers(self, end_date=datetime.date.today().strftime('%Y-%m-%d')):
		result = 0
		result += sum(x.amount for x in Donation.objects.filter(account=self, donation_date__lte=end_date))
		result -= sum(x.amount for x in Withdrawal.objects.filter(account=self, date__lte=end_date))
		return result

	def get_balance(self, start_date=None, end_date=None):
		result = 0
		result += self.sum_total_transfers(start_date)
		result += sum(x.amount for x in Donation.objects.filter(account=self, donation_date__range=(start_date, end_date)))
		result -= sum(x.amount for x in Withdrawal.objects.filter(account=self, date__range=(start_date, end_date)))
		#str(self.get_balance(start_date='2016-03-01', end_date='2016-03-31'))
		return result

	def __str__(self):
		return self.name + " (Q."+ str(self.credit)+")" 

class Withdrawal(models.Model):
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField(null=True, blank=True)
	purpose = models.ForeignKey('WithdrawalPurpose', on_delete=models.PROTECT)
	account = models.ForeignKey('Account', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return "Q." + str(self.amount) + " para " + self.purpose.name

@receiver(post_save, sender=Withdrawal, dispatch_uid="update_accout_debit")
def update_credit_withdrawal(sender, instance, **kwargs):
	instance.account.credit -= instance.amount
	instance.account.save()

class WithdrawalPurpose(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name