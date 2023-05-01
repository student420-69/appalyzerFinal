# Definimos otra tabla de la base de datos la cual es la de perfil del usuario
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Modelo perfil para crear usuarios nuevos
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # metodo para que la imagen usada por el usuario sea guardado en tamaño especifico y no ocupe mas memoria de la necesaria.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
