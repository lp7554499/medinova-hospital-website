from django.contrib import admin
from .models import Contact, Appointment
from django.urls import path
from .admin_dashboard import admin_dashboard
# from django.contrib import admin


urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin-dashboard"),
]



admin.site.register(Contact)
admin.site.register(Appointment)
# admin.site.urls = urlpatterns + admin.site.urls
