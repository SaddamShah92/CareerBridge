from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', views.job_list, name = 'job_list'),
    path('<int:job_id>/', views.job_detail, name = 'job_detail'),
    path('post/', views.post_job, name = 'post_job'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name = 'apply_for_job'),
    path('job/<int:job_id>/applications/', views.job_applications, name = 'job_applications'),
    path('about/', views.about_us, name = 'about_us'),
    path('contact/', views.contact, name = 'contact'),
    path('all_applications/', views.all_applications, name = 'all_applications'),
    path('application/<int:application_id>/shortlist/', views.toggle_shortlist, name='toggle_shortlist'),
]



