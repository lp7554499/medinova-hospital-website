from django.shortcuts import render
from ourdoctors.models import Doctor

def our_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'team.html', {'doctors': doctors})
