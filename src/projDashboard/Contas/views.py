from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import PasswordChangeCustomForm, EditUserForm, UserCreationCustomForm
from django.contrib.auth import update_session_auth_hash

class CadastroView(generic.CreateView):
    form_class = UserCreationCustomForm
    success_url = reverse_lazy('Entrada')
    template_name = 'Contas/cadastro.html'

@login_required
def SaidaView(request):
    logout(request)

    return redirect('Entrada')

@login_required
def EditUserView(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('Perfil'))
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'Contas/edit_username.html', {'form': form})

@login_required
def TrocSenhaView(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Atualiza a sessão do usuário para evitar que ele seja deslogado
            return redirect(reverse_lazy('Perfil'))
    else:
        form = PasswordChangeCustomForm(request.user)
    return render(request, 'Contas/edit_senha.html', {'form': form})

@login_required
def VisualPerfilView(request):
    return render(request, 'Contas/perfil.html', {'user': request.user})
