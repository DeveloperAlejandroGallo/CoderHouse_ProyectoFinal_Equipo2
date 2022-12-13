from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
def post_edit(request, id):
    post = Post.objects.get(id=id)

    lista_usuarios = User.objects.all()

    if request.method == 'POST':

        postEditForm = PostCrearForm(request.POST)

        if (postEditForm.is_valid()):

            data = postEditForm.cleaned_data

            post.titulo = data['titulo']
            post.subtitulo = data["subtitulo"]
            post.cuerpo = data["cuerpo"]
            post.fecha = data['fecha']
            post.imagen = data["imagen"]

            post.save()
            
            postslist = Post.objects.all().order_by('-fecha')

            return render(request, 'appBlog/post_list.html', {"postslist": postslist})

        else:

            postEditForm = PostCrearForm()
            return render(request, 'appBlog/post_edit.html', 
            {"postEditForm": postEditForm, "mensaje": ['Datos ingresados inválidos.']})

    else: 

        postEditForm = PostCrearForm(initial={
                'titulo':   post.titulo,
                'subtitulo':post.subtitulo,
                'cuerpo':   post.cuerpo ,
                'fecha':    post.fecha ,
                'imagen':   post.imagen 
            })
        
        return render(request, 'appBlog/post_edit.html', {"postEditForm": postEditForm, "id":id})    


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

def post_delete(request, pk):

    post = Post.objects.filter(id=pk)

    if post:
        post.delete()
        

    return render(request, 'appBlog/post_list.html',{'mensaje': 'Post Eliminado'})



#hecho con vistas
class PostList(LoginRequiredMixin, ListView):

    model = Post
    template_name = 'appBlog/posts_list.html'


class PostDetailView(DetailView):

    model = Post
    template_name = 'appBlog/post_detalle.html'

class PostDeleteView(DeleteView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('Posts_list/', views.PostList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Post
    success_url = '/Posts_list'


class PostUpdateView(UpdateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('Posts_list/', views.PostList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Post
    success_url = '/Posts_list'
    fields = ['nombre', 'comision']


class PostCreateView(LoginRequiredMixin, CreateView):

    # Recordatorio, en success_url utilzar el nombre de la url
    # Ejemplo:
    # path('Posts_list/', views.PostList.as_view(), name='List'),
    # en este caso, utilizar el string del primer parametro
    # antecedido de una slash
    model = Post
    success_url = '/Posts_list'
    fields = ['nombre', 'comision']

class EditPostView(UpdateView):
    model = Post
    from_class = PostAddForm
    template_name = 'appBlog/post_edit.html'
    success_url = '/post_list/'


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



