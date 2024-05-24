from django.contrib.admin import widgets
from django.db import models
from .functions import orderIdGen
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget,AdminSplitDateTime

# Create your models here.

class ReserveTable(models.Model):
	orderId = models.IntegerField(null=True, blank=True)
	name = models.CharField(max_length=50,null=True, blank=True)
	totalNumber = models.IntegerField(null=True, blank=True)
	email =models.EmailField(null=True, blank=True)
	phNo= models.IntegerField(null=True, blank=True)
	resDate = models.DateField(null=True, blank=True)
	resTime = models.TimeField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def save(self , *args , **kwargs):
		if not self.orderId and self.name:
			self.orderId = orderIdGen()
		super(ReserveTable , self).save(*args , **kwargs)

	class Meta:
		verbose_name = 'reservation'
		verbose_name_plural = 'reservations'


	def __str__(self):
		try:
			return self.name
		except:
			return "error"