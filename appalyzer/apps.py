#Configuración propia de Django para que el proyecto sea ejecutado
from django.apps import AppConfig

class AppalyzerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appalyzer'
