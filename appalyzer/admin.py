# En este archivo se hace la configuración necesaria para la página de
# administración del sitio
# Librerias necesarias para trabajar con la página de administrador de sitio
from django.contrib import admin
from .models import Search

# Asignamos el titulo de la página al nombre del proyecto
admin.site.site_header = "AppAlyzer"

admin.site.register(Search)