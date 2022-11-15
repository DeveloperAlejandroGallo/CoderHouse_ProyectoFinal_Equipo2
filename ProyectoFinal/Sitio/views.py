from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Persona
from django.db import *



def mostrar_personas(response):
    personas = Persona.objects.all() #Trae todos los registros de la base como una lista
    return render(response,'personas.html',{'personas':personas})

def inicio(response):
    return render(response,'index.html') #Acepta diccionarios

def funcion_con_parametros(response):
    lista = [1,2,3,4]
    return render(response, 'prueba.html',{'lista':lista})

def crear_cursos(response):
    return render(response,'crear_curso.html',{'curso':Curso})



