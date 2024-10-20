from django.db import models

from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    enquiry = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.date_submitted.strftime('%d-%m-%Y')}"