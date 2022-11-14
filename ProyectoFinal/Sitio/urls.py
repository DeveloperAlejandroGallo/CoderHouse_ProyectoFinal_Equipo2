from django.contrib import admin
from django.urls import path
from Sitio import views

urlpatterns = [
    path('',views.inicio),
    path('mostrar_persona/',views.mostrar_personas, name='Personas'),
    
]