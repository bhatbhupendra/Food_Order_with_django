from dataclasses import field
from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from meal.models import Meals

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class createMealForm(ModelForm):
	class Meta:
		model = Meals
		fields = ['name','description','category','price','option','isTodaySpecial','image']

