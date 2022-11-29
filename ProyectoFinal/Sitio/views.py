from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .models import *
from django.db import *
from .forms import *






def inicio(response):
    return render(response,'index.html') 

def blog(response):
    return render(response,'blog.html')

def about(response):
    return render(response,'about.html') 

def post_details(response):
    return render(response,'post-details.html') 

def contact(response):
    return render(response,'contact.html') 

def support(response):
    return render(response,'support.html') 

def login_request(request):

    if request.method=='POST':
        
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario ,password=contra)
            
            if user is not None:
                login(request,user)
            

                return render (request,'ingresar.html', {'mensaje':f'Bienvenido{usuario}'})
            else:

                return render (request,'ingresar.html',{'mensaje':f'El usuario no existe'})
        else:
            
                return render (request,'ingresar.html',{'mensaje':f'Error, formulario erroneo'})

    form = AuthenticationForm()

    return render (request,'registrarse.html',{'form':form})




class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'registrarse.html'


class AdminLoginView(LoginView):
    template_name = 'ingresar.html'

class AdminLogoutView(LogoutView):
    template_name = 'cerrar_sesion.html'


# def funcion_con_parametros(response):
#     lista = [1,2,3,4]
#     return render(response, 'prueba.html',{'lista':lista})

# def crear_profesor(request):
    
#     if request.method=='POST':

#         formulario=CrearProfesorForm(request.POST)

#         if formulario.is_valid():
            
#             formulario_limpio=formulario.cleaned_data
    
#             profesores=Profesor(
#                 nombre=formulario_limpio['nombre'],
#                 apellido=formulario_limpio['apellido'],
#                 edad=formulario_limpio['edad'],
#                 profesion=formulario_limpio['profesion'],
#                 email=formulario_limpio['email'])
            
#             profesores.save()
            
#             return render(request,'index.html')

#     else:
#         formulario=CrearProfesorForm()

#     return render(request,'crear_profesor.html',{'formulario':formulario})

# def buscar_profesor(request):

#     if request.GET.get('nombre',False):
#         nombre = request.GET['nombre'] 
#         profesores= Profesor.objects.filter(nombre__icontains=nombre)
        
#         if profesores.count() > 0:
#             return render (request,'buscar_profesor.html',{'profesores':profesores})
    
    
#     respuesta='Sin resultados'
#     return render(request,'buscar_profesor.html',{'respuesta': respuesta})


# def crear_cursos(request):
    
#     if request.method=='POST':

#         formulario=CrearCursoForm(request.POST)

#         if formulario.is_valid():
            
#             formulario_limpio=formulario.cleaned_data
    
#             curso=Curso(
#                 nombre=formulario_limpio['nombre'],
#                 codigo=formulario_limpio['codigo'],)
                
#             curso.save()
            
#             return render(request,'index.html')

#     else:
#         formulario=CrearCursoForm()

#     return render(request,'crear_curso.html',{'formulario':formulario})

# ###################################### Persona
# def crear_persona(request):
    
#     if request.method=='POST':

#         formulario=CrearPersonaForm(request.POST)

#         if formulario.is_valid():
            
#             formulario_limpio=formulario.cleaned_data
    
#             persona=Persona(
#                 nombre=formulario_limpio['nombre'],
#                 apellido=formulario_limpio['apellido'],
#                 edad=formulario_limpio['edad'],
#                 fecha_nacimiento=formulario_limpio['fecha_nacimiento'],
#                 email=formulario_limpio['email']
#                 ,dni=formulario_limpio['dni']
#                 )
            
#             persona.save()
            
#             return render(request,'index.html')

#     else:
#         formulario=CrearPersonaForm()

#     return render(request,'crear_persona.html',{'formulario':formulario})

# def buscar_persona_dni(request):

#     if request.GET.get('dni',False):
#         dni = request.GET['dni'] 
#         personas= Persona.objects.filter(dni__icontains=dni)
        
#         if personas.count() > 0:
#             return render (request,'buscar_persona.html',{'personas':personas})
    
    
#     respuesta='Sin resultados'
#     return render(request,'buscar_persona.html',{'respuesta': respuesta})