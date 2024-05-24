from django.contrib.admin import widgets
from django.forms import ModelForm
from .models import ReserveTable
from django import forms

from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class reserveTableForm(ModelForm):
    class Meta:
        model = ReserveTable
        exclude = ['orderId']
        widgets = {
            "resDate": AdminDateWidget(),
            "resTime": AdminTimeWidget(),
        }
