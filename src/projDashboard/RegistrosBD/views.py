from django.contrib.auth.decorators import login_required
from .forms import RegistClienteForm, RegistProdutoForm, RegistVendaForm, RegistDespesaForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

@login_required
def regist_cliente_view(request):
    if request.method == 'POST':
        form = RegistClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('Dashboard'))
    else:
        form = RegistClienteForm()
    return render(request, 'regist-cliente.html', {'form': form})
