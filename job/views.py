from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Job, JobApplication
from django.contrib import messages
from .forms import JobForm, JobApplicationForm
from accounts.models import UserProfile
from django.views.decorators.http import require_POST


# Utility functions for role checking

def is_hr(user):
    return user.userprofile.role.lower() == 'hr'

def is_user(user):
    return user.userprofile.role.lower() == 'user'

def is_admin(user):
    return user.userprofile.role.lower() == 'admin'

#  Unified Job List View
def job_list(request):
    jobs = Job.objects.all().order_by('-date_of_posting')
    return render(request, 'job_list.html', {'jobs': jobs})

#  Job Detail View
def job_detail(request, job_id):
    job = get_object_or_404(Job, id = job_id)
    return render(request, 'job_detail.html', {'job' : job })

#  Post a Job (HR only)
@login_required
def post_job(request):
    if not is_hr(request.user):
        return HttpResponseForbidden("You are not authorized to post jobs.")
     
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_list')
        else:
            messages.error(request, "There was an error posting your job.")
    else:
        form = JobForm()    

    return render(request, 'add_job.html', {'form': form})

# Apply for a Job (User only)
@login_required
def apply_for_job(request, job_id):
    if not is_user(request.user):
        return HttpResponseForbidden("Only job seekers can apply for jobs.")
    
    job = get_object_or_404(Job, id = job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('job_list')
        else:
            messages.error(request, "There was an error submitting your application.")
                   
    else: 
        form = JobApplicationForm()

    return render(request, 'apply.html', {'form': form, "job": job})

# View Applications for a Job (Used by HR)
@login_required
def job_applications(request, job_id):
    job = get_object_or_404(Job, id = job_id)
    applications = JobApplication.objects.filter(job = job)
    return render(request, 'job_application.html', {'job': job, 'applications': applications})

# View My Applications (User only)
@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'my_applications.html', {'applications': applications})

# Delete My Applications
@login_required
def delete_application(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    application.delete()
    messages.success(request, "Application deleted successfully.")
    return redirect('my_applications') 

# For About Page
def about_us(request):
    return render(request, 'about_us.html')


# For Contact Page
def contact(request):
    return render(request, 'contact.html')


# For All Applications (Used by HR)                                                                                                                          
@login_required
def all_applications(request):
    applications = JobApplication.objects.select_related('job').order_by('-applied_at')
    return render(request, 'all_applications.html', {'applications' : applications})

# For Shortlist the Applicants
@login_required
@user_passes_test(is_hr)
def toggle_shortlist(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    application.is_shortlisted = not application.is_shortlisted
    application.save()
    return redirect('job_applications', job_id=application.job.id)

# For Shortlisted Applications
def all_shortlisted_applicants(request):
    shortlisted = JobApplication.objects.filter(is_shortlisted=True)
    return render(request, 'all_shortlisted_applicants.html', {'shortlisted': shortlisted})

# For Unshortlist Applications from Shortlisted Template
@require_POST
def unshortlist_applicant(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    application.is_shortlisted = False
    application.save()
    return redirect('all_shortlisted_applicants')
