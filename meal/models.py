import imp
from pyexpat import model
from random import choice
from tkinter import Widget
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from account.models import Customer

from django import forms
# Create your models here.

class Meals(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	description = models.TextField(max_length=500, null=True, blank=True)
	category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
	price = models.DecimalField(max_digits=5 , decimal_places=2)
	option = models.IntegerField(null=True, blank=True)
	isTodaySpecial = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(upload_to='meals/')
	slug = models.SlugField(blank=True, null=True)


	def save(self , *args , **kwargs):
		if not self.slug and self.name :
			self.slug = slugify(self.name)
		super(Meals , self).save(*args , **kwargs)

	class Meta:
		verbose_name = 'meal'
		verbose_name_plural = 'meals'


	def __str__(self):
		return self.slug

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Category(models.Model):
	name = models.CharField(max_length=30)


	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	submited = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.customer.user.username + "-" + str(self.id))

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total


class OrderItem(models.Model):
	product = models.ForeignKey(Meals, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=1, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)



	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

	def __str__(self):
		return str(self.product.name)



SPICY_LEVAL = [
        ('regular','Regular'),
        ('mild', 'Mild'),
        ('hot', 'Hot'),
        ('blend_hot', 'Blend Hot'),
        ('spicy', 'Spicy'),
    ]

class optionOneOptions(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	price = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Option One Items'
		verbose_name_plural = 'Option One Items'

	def __str__(self):
		return self.name

class optionTwoOptions(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	price = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name = 'Option Two Item'
		verbose_name_plural = 'Option Two Items'

	def __str__(self):
		return self.name
 
class optionOne(models.Model):
	orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
	foodChoice = models.ForeignKey(optionOneOptions, on_delete=models.CASCADE, null=True, blank=True)
	spicy = models.CharField(choices=SPICY_LEVAL, null=True, blank=True, max_length=50)

	class Meta:
		verbose_name = 'Option One'
		verbose_name_plural = 'Option One'

	def __str__(self):
		return str("OptionOne")

class optionTwo(models.Model):
	orderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)
	foodChoice = models.ForeignKey(optionTwoOptions, on_delete=models.CASCADE, null=True, blank=True)
	spicy = models.CharField(choices=SPICY_LEVAL, null=True, blank=True, max_length=50)

	class Meta:
		verbose_name = 'Option Two'
		verbose_name_plural = 'Option Two'

	def __str__(self):
		return str("OptionTwo")



