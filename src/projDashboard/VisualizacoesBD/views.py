from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Central.models import Cliente, Produto, Venda, Despesa

@login_required
def visual_clientes_view(request):
    clientes = Cliente.objects.all()

    return render(request, 'VisualizacoesBD/visual-clientes.html', {'clientes': clientes})

@login_required
def visual_produtos_view(request):
    produtos = Produto.objects.all()

    return render(request, 'VisualizacoesBD/visual-produtos.html', {'produtos': produtos})

@login_required
def visual_vendas_view(request):
    vendas = Venda.objects.all()

    return render(request, 'VisualizacoesBD/visual-vendas.html', {'vendas': vendas})

@login_required
def visual_despesas_view(request):
    despesas = Despesa.objects.all()

    return render(request, 'VisualizacoesBD/visual-despesas.html', {'despesas': despesas})
