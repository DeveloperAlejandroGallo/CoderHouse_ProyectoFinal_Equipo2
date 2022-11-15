from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView



def mostrar_personas(response):
    personas = Persona.objects.all() #Trae todos los registros de la base como una lista

    return render(response,'personas.html',{'personas':personas})

def inicio(response):
    return render(response,'index.html') #Acepta diccionarios

def funcion_con_parametros(response):
    lista = [1,2,3,4]
    return render(response, 'prueba.html',{'lista':lista})

class CursoList(ListView):
    model = Curso
    template_name = 'cursos_list.html'

class CursoDetail(DetailView):
    model = Curso
    template_name = 'cursos_detalle.html'