from django.shortcuts import render, redirect
from .forms import ApplicantForm
from .models import Applicant
from .utils import parse_resume, match_with_jobs

def apply_job(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            applicant = form.save()
            keywords = parse_resume(applicant.resume.path)
            match_score = match_with_jobs(keywords, applicant.job_domain)
            if match_score >= 60:
                applicant.eligibility_status = True
                applicant.save()
            return redirect('success_page')
    else:
        form = ApplicantForm()
    return render(request, 'applicant/apply.html', {'form': form})

def success_page(request):
    return render(request, 'applicant/success.html')
