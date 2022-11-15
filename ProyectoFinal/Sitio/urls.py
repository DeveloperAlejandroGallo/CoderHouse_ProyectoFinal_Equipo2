from django.contrib import admin
from django.urls import path
from Sitio import views

urlpatterns = [
    path('',views.inicio),
    path('mostrar_persona/',views.mostrar_personas, name='Personas'),
    path('curso_list', views.CursoList.as_view(),),
    path('curso_detail', views.CursoDetail.as_view())
]