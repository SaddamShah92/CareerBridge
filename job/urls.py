from django.urls import path
from .views import job_detail, job_list

urlpatterns = [
    path('', job_list, name = 'job_list'),
    path('<int:job_id>/', job_detail, name = 'job_detail'),
]