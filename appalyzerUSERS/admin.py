# página de administracion del sitio donde se muestra el modelo ´Profile´para mostrar los perfiles registrados
from django.contrib import admin
from .models import Profile

# Modelo perfil registrado
admin.site.register(Profile)