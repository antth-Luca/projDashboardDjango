from django.urls import path
from .views import CadastroView, SaidaView, EditUserView, TrocSenhaView, VisualPerfilView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('cadastrar/', CadastroView.as_view(), name='Cadastro'),
    path('entrar/', LoginView.as_view(template_name='Contas/entrada.html'), name='Entrada'),
    path('sair/', SaidaView, name='Saida'),
    path('ver-perfil/', VisualPerfilView, name='Perfil'),
    path('editar/', EditUserView, name='EditarPerfil'),
    path('trocar-senha/', TrocSenhaView, name='TrocarSenha'),
]