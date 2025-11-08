from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allergies_list, name='allergy_list'), 
]