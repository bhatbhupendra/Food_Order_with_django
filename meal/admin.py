import imp
from django.contrib import admin
from .models import Meals, Category, Order, OrderItem
from .models import optionOneOptions, optionTwoOptions, optionOne, optionTwo
 
# Register your models here.
admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(optionOneOptions)
admin.site.register(optionTwoOptions)
admin.site.register(optionOne)
admin.site.register(optionTwo)
