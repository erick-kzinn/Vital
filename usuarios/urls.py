from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.logar, name="login"),  
    path('cadastro/', views.cadastro, name="cadastro"),
    path('sair/', views.sair, name="sair"),

]