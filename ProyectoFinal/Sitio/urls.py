from django.contrib import admin
from django.urls import path
from Sitio import views

urlpatterns = [
    path('',views.inicio),
    path('index.html', views.inicio),
    path('blog.html', views.blog),
    path('about.html', views.about),
    path('post-details.html', views.post_details),
    path('contact.html', views.contact),
    # path('admin/', admin.site.urls, name='Admin'),
    # path('crear_curso/',views.crear_cursos, name='Curso'),
    # path('crear_profesor/', views.crear_profesor , name='Profesores'),
    # path('buscar_profesor/', views.buscar_profesor, name='BuscarProfesor'),
    # path('crear_persona/', views.crear_persona , name='Personas'),
    # path('buscar_persona/', views.buscar_persona_dni, name='BuscarPersona'),
    # path('mostrar_persona/',views.mostrar_personas, name='ListarPersonas'),
]