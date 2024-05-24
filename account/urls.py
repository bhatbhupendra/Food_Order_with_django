from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="account"

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

	path('adminSection/', views.adminSection, name="admin-section"),
	path('orderSection/', views.orderSection, name="order-section"),
	path('orderInfo/<str:pk>/', views.orderInfo, name="order-info"),

    # path('user/', views.userPage, name="userPage"),

    #path('account/', views.accountSettings, name="account"),


    #path('reset_password/', auth_views.PasswordResetView.as_view(template_name="pass_reset_templates/password_reset.html"), name="reset_password"),
    #path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="pass_reset_templates/password_reset_sent.html"), name="password_reset_done"),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="pass_reset_templates/password_reset_form.html"), name="password_reset_confirm"),
    #path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="pass_reset_templates/password_reset_done.html"), name="password_reset_complete"),
]
