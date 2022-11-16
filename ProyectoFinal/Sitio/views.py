from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Persona, Profesor
from django.db import *
from .forms import CrearProfesorForm 




def mostrar_personas(response):
    personas = Persona.objects.all() #Trae todos los registros de la base como una lista
    return render(response,'personas.html',{'personas':personas})

def inicio(response):
    return render(response,'index.html') #Acepta diccionarios

def funcion_con_parametros(response):
    lista = [1,2,3,4]
    return render(response, 'prueba.html',{'lista':lista})

def crear_profesor(request):
    
    if request.method=='POST':

        formulario=CrearProfesorForm(request.POST)

        if formulario.is_valid():
            
            formulario_limpio=formulario.cleaned_data
    
            profesores=Profesor(
                nombre=formulario_limpio['nombre'],
                apellido=formulario_limpio['apellido'],
                edad=formulario_limpio['edad'],
                profesion=formulario_limpio['profesion'],
                email=formulario_limpio['email'])
            
            profesores.save()
            
            return render(request,'index.html')

    else:
        formulario=CrearProfesorForm()

    return render(request,'crear_profesor.html',{'formulario':formulario})

def buscar_profesor(request):

    if request.GET.get('nombre',False):
        nombre = request.GET['nombre'] 
        profesores= Profesor.objects.filter(nombre__icontains=nombre)
        
        if profesores.count() > 0:
            return render (request,'buscar_profesor.html',{'profesores':profesores})
    
    
    respuesta='Sin resultados'
    return render(request,'buscar_profesor.html',{'respuesta': respuesta})



