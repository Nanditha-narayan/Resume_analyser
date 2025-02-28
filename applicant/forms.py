from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    job_domain_choices = [
        ('Software Engineering', 'Software Engineering'),
        ('Data Science', 'Data Science'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
    ]

    job_domain = forms.ChoiceField(choices=job_domain_choices)
    
    class Meta:
        model = Applicant
        fields = ['name', 'contact', 'email', 'job_domain', 'resume']
