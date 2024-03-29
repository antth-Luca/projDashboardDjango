from django.urls import path
from .views import CadastroView, SaidaView, EditUserView, VisualPerfilView
from django.contrib.auth.views import LoginView
from .forms import AuthenticationCustomForm

urlpatterns = [
    path('cadastrar/', CadastroView.as_view(), name='Cadastro'),
    path('entrar/', LoginView.as_view(form_class=AuthenticationCustomForm, template_name='Contas/entrada.html'), name='Entrada'),
    path('sair/', SaidaView, name='Saida'),
    path('ver-perfil/', VisualPerfilView, name='Perfil'),
    path('editar/', EditUserView, name='EditarPerfil'),
]