from django.urls import path
from . import views

app_name = 'home'  
urlpatterns = [
    path('', views.index, name='index'),
    path('celulares/', views.celulares, name='celulares'),
    path('computadores/', views.computadores, name='computadores'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('adicionar_celular/', views.adicionar_celular, name='adicionar_celular'), 
    path('adicionar_computador/', views.adicionar_computador, name='adicionar_computador'), 
    path('perfil/<int:id>/', views.perfil, name='perfil'),
    path('cadastro_colaborador/', views.adicionar_colaborador, name='cadastro_colaborador'),
    path('excluir_computador/<int:id>/', views.excluir_computador, name='excluir_computador'),
    path('excluir_celular/<int:id>/', views.excluir_celular, name='excluir_celular'),
     path('excluir_colaborador/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
]

