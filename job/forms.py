from django import forms
from .models import Job, JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'salary', 'job_type','description']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applicant_name', 'email', 'resume', 'cover_letter']
        widgets = {
            'cover_letter' : forms.Textarea(attrs={'row': 4}),
        }