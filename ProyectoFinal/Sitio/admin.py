from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Curso) # Esto es para poder tener usar el admin con esta clase curso???
