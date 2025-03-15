from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def job_list(request):
    jobs = Job.objects.all().order_by('-date_of_posting')
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id = job_id)
    return render(request, 'job_detial.html', {'job' : job })
