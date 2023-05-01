#Se definen los paths a seguir y su propio correspondiente, permitiendo
# definir las urls validas
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, UserPostListView
from . import views

#Todas las urls necesarias para el funcionamiento del proyecto
urlpatterns = [
    path('', views.home, name='AppAlyzer-Home'),
    path('user/<str:username>', UserPostListView.as_view(), name='AppAlyzer-UserPosts'),
    path('posts/', PostListView.as_view(), name='AppAlyzer-Posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='AppAlyzer-PostDetails'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='AppAlyzer-PostDelete'),
    path('analyzer/', PostCreateView.as_view(), name='AppAlyzer-Analyzer'),
    path('contact/', views.contact, name='AppAlyzer-Contact'),
]