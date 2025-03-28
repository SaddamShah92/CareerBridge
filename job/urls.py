from django.urls import path
from .views import custom_login
from . import views

urlpatterns = [
    path('', views.job_list, name = 'job_list'),
    path('<int:job_id>/', views.job_detail, name = 'job_detail'),
    path('add/', views.add_job, name = 'add_job'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name = 'apply_for_job'),
    path('job/<int:job_id>/applications/', views.job_applications, name = 'job_applications'),
    path('register/', views.registration, name = 'register'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name = 'logout'),
    path('about/', views.about_us, name = 'about_us'),
    path('contact/', views.contact, name = 'contact'),
]



