from django.urls import path
from django.contrib.auth import views as auth_views
from .views import job_detail, job_list, add_job, apply_for_job, job_applications, registration ,custom_logout
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', job_list, name = 'job_list'),
    path('<int:job_id>/', job_detail, name = 'job_detail'),
    path('add/', add_job, name = 'add_job'),
    path('job/<int:job_id>/apply/', apply_for_job, name = 'apply_for_job'),
    path('job/<int:job_id>/applications/', job_applications, name = 'job_applications'),
    path('register/', registration, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', custom_logout, name = 'logout'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

