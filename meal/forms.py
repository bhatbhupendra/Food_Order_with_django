from django.forms import ModelForm
from .models import *

class optionOneForm(ModelForm):
	class Meta:
		model = optionOne
		fields = ['foodChoice','spicy']

class optionTwoForm(ModelForm):
	class Meta:
		model = optionTwo
		fields = ['foodChoice','spicy']