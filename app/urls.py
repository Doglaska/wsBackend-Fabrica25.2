from django.urls import path
from . import views
from .views import listarAlunos, criarAluno, atualizarAluno, deletarAluno, listarProfessores, criarProfessor, atualizarProfessor, deletarProfessor, localizarIp

urlpatterns = [
    path('', views.home, name='home'),
    path('listar', listarAlunos, name='listarAlunos'),
    path('criar', criarAluno, name='criarAluno'),
    path('atualizar/<int:pk>', atualizarAluno, name='atualizarAluno'),
    path('deletar/<int:pk>', deletarAluno, name='deletarAluno'),
    
    path('listarP', listarProfessores, name='listarProfessores'),
    path('criarP', criarProfessor, name='criarProfessor'),
    path('atualizarP/<int:pk>', atualizarProfessor, name='atualizarProfessor'),
    path('deletarP/<int:pk>', deletarProfessor, name='deletarProfessor'),

    path('localizar', localizarIp, name='localizarIp'),
]