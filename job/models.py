from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    JOB_TYPES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    ]
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null= True, blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='Full-time')
    date_of_posting = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date_of_posting']
        verbose_name = 'Job Posting'
        verbose_name_plural = 'Job Postings'
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    applicant_name = models.CharField(max_length= 100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/%Y/%m/%d/')
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    is_shortlisted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.applicant_name} - {self.job.title}'
    
    class Meta:
        ordering = ['-applied_at']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'


