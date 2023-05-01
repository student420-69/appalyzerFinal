# archivo donde son renderizadas las vistas a sus respectivos urls ademas
# de procesos internos que son necesarios para el propio funcionamiento del sistema
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SetPasswordForm

# Create your views here.
# vista donde valida que los campos para registrarse hayan sido completados satisfactoriamente
# y retorna un mensaje de exito o error respectivamente
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cuenta creada con éxito. Inicia sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'appalyzerUSERS/register.html', {'form': form})

# vista para actualizar el perfil del usuario
@login_required # validar que usuario este iniciado sesión
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Información actualizada')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'appalyzerUSERS/profile.html', context)
