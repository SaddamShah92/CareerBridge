from django.db import models

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
    



