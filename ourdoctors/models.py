from django.db import models

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=250)
    doctor_post = models.CharField(max_length=250)
    doctor_img = models.ImageField(upload_to="doctors", blank=True, null=True)

    def __str__(self):
        return self.doctor_name