from django.urls import path
from users.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register', register_customer, name='register_customer'),
    
    path('register_staff', register_staff, name='register_staff'),
    
    path('dashboard', customer_dashboard, name='customer_dashboard'),
    
    path('staff_dashboard', staff_dashboard, name='staff_dashboard'),
    
    path('profile', customer_profile, name='customer_profile'),
    
    path('staff_profile', staff_profile, name='staff_profile'),
    
    path('redirecting', post_login, name='post_login'),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.htm'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.htm'), name='logout'),
    
]
