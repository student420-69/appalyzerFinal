# Se definen los formularios personalizados necesarios para cada funcionalidad del sistema
# podemos definir los campos que son necesarios llenar para que sean completados satisfactoriamente
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model
from .models import Profile

# Formulario para registrar nuevo usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(), 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario para actualizar usuario o correo de usuario
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(), 
    class Meta:
        model = User
        fields = ['username', 'email']

#Formulario para actualizar la imagen de perfil
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
