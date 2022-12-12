from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Redireccion
from django.urls import reverse_lazy
# Auth
from django.contrib.auth.views import LoginView, LogoutView

#Los decoradores sirven para funciones > vistas basadas en funciones
from django.contrib.auth.decorators import login_required

#ejemplo
# @decorador
# def funcion_a_proteger

#Los mixins sirven para clases > vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

from appBlog.forms import *
from appBlog.models import *
from appUsuarios.models import *



def inicio(request):
    if request.user.username:

        userData = UserData.objects.filter(user=request.user)

        user = request.user
        return render(request,'appBlog/index.html', {'user':user,'userData':userData}) 
    else:
        return render(request,'appBlog/index.html', {'user':None,'userData':None}) 



def about(request):
    return render(request,'appBlog/about.html') 

def contact(request):
    return render(request,'appBlog/contact.html') 

@login_required
def post_edit(request, pk):

    post = Post.objects.get(id=pk)

    if request.method == "POST":

        postEditForm = PostCrearForm(request.POST)
        
        if postEditForm.is_valid():

            data = postEditForm.cleaned_data

            post.titulo = data['titulo']
            post.subtitulo = data["subtitulo"]
            post.cuerpo = data["cuerpo"]
            post.imagen = data["imagen"]

            post.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, "appBlog/post_list.html", {'postlist': postslist})

        else:

            # postEditForm = PostCrearForm()

            return render(request, "appBlog/post_edit.html", {"formulario": postEditForm, "errors": ['Datos ingresados inválidos.']})

    else:

        postEditForm = PostCrearForm(initial={"titulo": post.titulo, "subtitulo": post.subtitulo, 'cuerpo': post.cuerpo, 'imagen': post.imagen.url})

        return render(request, "appBlog/post_edit.html", {"formulario": postEditForm})



def post_create(request):

    if( request.method == "POST"):

        postCreateForm = PostCrearForm(request.POST, request.FILES)
        postCreateForm.usuario = request.user.username
        if(postCreateForm.is_valid()):

            content = postCreateForm.cleaned_data

            post = Post(
                usuario = request.user,
                titulo = content['titulo'],
                subtitulo = content['subtitulo'],
                fecha = content['fecha'],
                imagen = content['imagen'],
                cuerpo = content['cuerpo'],
                likes = 0
            )

            post.save()

            postslist = Post.objects.all().order_by('-fecha')

            return render(request, 'appBlog/post_list.html', {"postslist": postslist})

        else:
            
            return render(request, 'appBlog/post_create.html', {"postCreateForm": postCreateForm, "mensaje": ['Datos ingresados Erróneos']})

    else:
        postCreateForm = PostCrearForm()
        return render(request, 'appBlog/post_create.html', {"postCreateForm": postCreateForm}) 


def post_list(request):
    postslist= Post.objects.all().order_by('-fecha')
    
    if postslist.count() > 0:
        return render(request, 'appBlog/post_list.html', {"postslist": postslist})
    
    respuesta='Aún no hay Posteos para mostrar'
    return render(request, 'appBlog/post_list.html',{'mensaje': respuesta})




def post_find(request):
    
    if request.GET.get('busqueda',False):
        busqueda = request.GET['busqueda'] 
        postslist= Post.objects.all().filter(titulo__icontains=busqueda).order_by('-fecha')
      
        if postslist.count() > 0:
            return render(request, 'appBlog/post_find.html', {"postslist": postslist})
  
  
    respuesta='Sin resultados'
    return render(request, 'appBlog/post_find.html',{'mensaje': respuesta})




# def contactView(request):
#     if request.method == "GET":
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             asunto = form.cleaned_data["asunto"]
#             email = form.cleaned_data["email"]
#             mensaje = form.cleaned_data['mensaje']
#             try:
#                 send_mail(asunto, email, mensaje, ["aleveliz75@gmail.com"])
#             except BadHeaderError:
#                 return HttpResponse("Inválido.")
#             return redirect("Enviado")
#     return render(request, "appBlog/contact.html", {"form": form})

# def successView(request):
#     return HttpResponse("Enviado! Gracias por tu mensaje!.")



