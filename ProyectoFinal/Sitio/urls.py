from django.contrib import admin
from django.urls import path
from Sitio import views

urlpatterns = [
    path('',views.inicio),
    path('mostrar_persona/',views.mostrar_personas, name='Personas'),
    path('crear_curso/',views.crear_cursos, name='Curso'),
    path('crear_profesor/', views.crear_profesor , name='Profesores'),
    path('buscar_profesor/', views.buscar_profesor, name='Buscar Profesor'),
]