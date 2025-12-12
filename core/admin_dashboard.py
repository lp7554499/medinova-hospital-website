from django.contrib import admin
from django.urls import path
from medicine.models import Medicine

def admin_dashboard(request):
    total_medicines = Medicine.objects.count()
    categories = Medicine.objects.values('category').distinct().count()
    latest_medicines = Medicine.objects.order_by('-id')[:5]

    context = {
        "total_medicines": total_medicines,
        "categories": categories,
        "latest_medicines": latest_medicines,
    }

    return admin.site.admin_view(admin_dashboard_template)(request, context)


def admin_dashboard_template(request, context):
    from django.shortcuts import render
    return render(request, "dashboard.html", context)
