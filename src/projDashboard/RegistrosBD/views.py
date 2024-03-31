from django.contrib.auth.decorators import login_required
from .forms import RegistClienteForm, RegistProdutoForm, RegistVendaForm, RegistDespesaForm
from Central.models import Venda, Vendedor, Cliente, Produto
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

@login_required
def regist_cliente_view(request):
    if request.method == 'POST':
        form = RegistClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('VisualClientes'))
    else:
        form = RegistClienteForm()
    return render(request, 'RegistrosBD/regist-cliente.html', {'form': form})


@login_required
def regist_produto_view(request):
    if request.method == 'POST':
        form = RegistProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('VisualProdutos'))
    else:
        form = RegistProdutoForm()
    return render(request, 'RegistrosBD/regist-produto.html', {'form': form})

@login_required
def regist_venda_view(request):
    if request.method == 'POST':
        form = RegistVendaForm(request.POST)
        if form.is_valid():
            vendedor = Vendedor.objects.get(nome=form.cleaned_data['vendedor'])
            cliente = Cliente.objects.get(nome=form.cleaned_data['cliente'])
            produto = Produto.objects.get(nome=form.cleaned_data['produto'])
            quantidade = form.cleaned_data['quantidade']

            Venda.objects.create(vendedor=vendedor, cliente=cliente, produto=produto, total=produto.preco * quantidade)
            return redirect(reverse_lazy('VisualVendas'))
        else:
            print(form.errors)
    else:
        form = RegistProdutoForm()
    return render(request, 'RegistrosBD/regist-venda.html', {'form': form})

@login_required
def regist_despesa_view(request):
    if request.method == 'POST':
        form = RegistDespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('VisualDespesas'))
    else:
        form = RegistDespesaForm()
    return render(request, 'RegistrosBD/regist-despesa.html', {'form': form})