#Configuración propia de Django para ejecutar programa
from django.apps import AppConfig


class AppalyzerusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appalyzerUSERS'

    def ready(self):
        import appalyzerUSERS.signals
