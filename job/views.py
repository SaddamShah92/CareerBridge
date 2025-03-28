from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job, JobApplication
from .forms import JobForm, JobApplicationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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
            messages.success(request, "Your application has been submitted successfully!")
        else:
            messages.error(request, "There was an error submitting your application.")
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
            messages.success(request, "Your application has been submitted successfully!")
        else:
            messages.error(request, "There was an error submitting your application.")
                   
            return redirect('job_list')

    else: 
        form = JobApplicationForm()

    return render(request, 'apply.html', {'form': form, "job": job})

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
            messages.success(request, "You have registered successfully!")
            return redirect('custom_login')
        else:
            messages.error(request, "This username is already registered")     

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("job_list")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "users/custom_login.html")


def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("custom_login")

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')



