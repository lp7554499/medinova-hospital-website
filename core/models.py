from django.db import models
from django.utils import timezone


# Contact form ka model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255, default="No Subject")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Appointment form model
class Appointment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True)   # default value added
    time = models.TimeField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True) 
    doctor = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        name = self.name if self.name else "Unknown"
        date = self.date.strftime("%Y-%m-%d") if self.date else "No Date"
        return f"Appointment with {name} on {date}"
