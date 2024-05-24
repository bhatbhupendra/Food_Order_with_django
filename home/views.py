from django.shortcuts import render
from meal.models import Meals
# Create your views here.
def home(request):
    meals = Meals.objects.all()
    context={
        'meals': meals,
    }
    return render(request ,'home.html', context)