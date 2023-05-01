# Archivo donde son renderizadas las vistas a sus respectivos urls asi como
# asi como los procesos internos que realizan
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages
from django.template import loader
import appalyzer
import datetime
from .models import Search
from .analyzer_back import obtener_comentarios, polaridades, polaridad_total, emocion

def home(request):
    return render(request, 'appalyzer/index.html')

#Función para que el usuario se ponga en contacto con el usuario.
@csrf_exempt
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # Enviar correo - proceso
        send_mail(subject, message,email,['appalyzer@outlook.com'])
        messages.success(request, f'Gracias por contactarnos, recibiras un correo pronto!')
        return render(request, 'appalyzer/contact.html', {'name': name})
    else:
        return render(request, 'appalyzer/contact.html')

#Función donde se muestran todas las predicciones realizadas
class PostListView(LoginRequiredMixin, ListView):
    context = { 
        'posts': Search.objects.all() 
    }
    model = Search
    template_name = 'appalyzer/posts.html' 
    context_object_name = 'posts'  
    ordering = ['-date_consulted']

#Función que retorna las predicciones hechas por el mismo usuario.
class UserPostListView(LoginRequiredMixin, ListView):
    context = { 
        'posts': Search.objects.all() 
    }
    model = Search
    template_name = 'appalyzer/user_posts.html' 
    context_object_name = 'posts'  
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Search.objects.filter(author=user).order_by('-date_consulted')

#Función que retorna los datos necesarios para cuando queremos ver los detalles de una predicción
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Search 
    template_name = 'appalyzer/post_details.html' 

#Función que se conecta con analyzer_back.py para extrar los datos
# y en esta función son ingresados en sus respectivos campos de la base de datos.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Search 
    fields = ['ID_App', 'Cantidad_Comentarios']
    template_name = 'appalyzer/analyzer.html' 
    def form_valid(self, form):
        form.instance.author = self.request.user
        appName = form.cleaned_data['ID_App']
        commentsQuantity = form.cleaned_data['Cantidad_Comentarios']
        comentarios = obtener_comentarios(appName, commentsQuantity)
        form.instance.ID_App = comentarios[0]
        polaridad = polaridades(comentarios, commentsQuantity)
        polaridadT = polaridad_total(polaridad)
        form.instance.positive_comments = polaridadT[0]
        form.instance.neutral_comments = polaridadT[1]
        form.instance.negative_comments = polaridadT[2]
        form.instance.emotion_comments = emocion(comentarios)
        return super().form_valid(form)

#Función que retorna los detalles necesarios para eliminar una publicación.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Search 
    template_name = 'appalyzer/post_delete.html'
    success_url = '/posts' 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        