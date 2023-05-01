#Se definen las señales las cuales son alertas enviadas por procesos internos y despues mostradas en pantalla
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# retorna perfil en cuanto fue creado
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# guarda perfil en cuanto fue creado
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()