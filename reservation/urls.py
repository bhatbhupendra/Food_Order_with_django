from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="reservation"

urlpatterns = [
	path('', views.reservation, name="reservation-list"),
]