# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name='register'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='logout'),

    
]
