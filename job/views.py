from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def job_list(request):
    jobs = Job.objects.all().order_by('-date_of_posting')
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id = job_id)
    return render(request, 'job_detail.html', {'job' : job })

def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')    
    else:
        form = JobForm()

    return render(request, 'add_job.html', {'form': form})

def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id = job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_list')

    else: 
        form = JobApplicationForm()

    return render(request, 'apply.html', {'form': form})

def job_applications(request, job_id):
    job = get_object_or_404(Job, id = job_id)
    applications = JobApplication.objects.filter(job = job)

    return render(request, 'job_application.html', {'job': job, 'applications': applications})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')




