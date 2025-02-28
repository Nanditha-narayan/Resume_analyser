from djongo import models
import datetime

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    job_domain = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(default=datetime.datetime.now)
    eligibility_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
