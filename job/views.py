from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm

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
