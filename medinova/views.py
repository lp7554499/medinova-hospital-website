from django.shortcuts import render, get_object_or_404
from medicine.models import Medicine


def medicines_page(request):
    medicines = Medicine.objects.all()
    return render(request, "medicines.html", {"medicines": medicines})
