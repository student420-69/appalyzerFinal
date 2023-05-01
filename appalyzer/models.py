# Archivo donde se define la base de datos, los campos establecidos asi como su tipo
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Se crea el modelo Search donde se establecen todos los campos necesarios para que se 
# guarden los datos cuando se hace una busqueda
class Search(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_App = models.CharField(max_length=30)
    Cantidad_Comentarios = models.IntegerField()
    positive_comments = models.IntegerField()
    neutral_comments = models.IntegerField()
    negative_comments = models.IntegerField()
    emotion_comments = models.CharField(max_length=30)
    date_consulted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ID_App

    def get_absolute_url(self):
        return reverse('AppAlyzer-PostDetails', kwargs={'pk':self.pk})
        

