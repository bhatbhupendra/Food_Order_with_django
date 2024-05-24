from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="meal"

urlpatterns = [
	path('', views.meal_list, name="meal_list"),
	path('checkout/', views.checkout, name="checkout"),
	path('creatorder/<str:slug>/', views.createOrder, name="create_order"),
	path('update-choices/<str:pk>/', views.updateChoices, name="update_choice"),
	path('increase-order-qty/<str:slug>/', views.increaseOrderQty, name="increase_order_qty"),
	path('decrease-order-qty/<str:slug>/', views.decreaseOrderQty, name="decrease_order_qty"),
	path('delete-order-item/<str:slug>/', views.deleteOrderItem, name="delete_order_item"),
	path('submit-order/', views.submitOrder, name="submit_order"),

]