from django.db import models

class CoverLetter(models.Model):
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"Cover Letter for {self.job_title} by {self.full_name}"
