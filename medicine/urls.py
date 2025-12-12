from django.urls import path
from . import views

urlpatterns = [
    path('', views.medicines_list),       # GET + POST
    path('<int:id>/', views.medicine_detail),  # GET + PUT + PATCH + DELETE
]
