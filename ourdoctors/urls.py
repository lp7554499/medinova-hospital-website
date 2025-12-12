from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_doctors, name='our_doctors'),
]
