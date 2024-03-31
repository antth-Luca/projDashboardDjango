from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Central.models import Cliente, Produto, Venda, Despesa

@login_required
def visual_clientes_view(request):
    clientes = Cliente.objects.all()
    dict_clientes = {}
    cont = 0
    for cliente in clientes:
        dict_clientes[cont] = cliente
        cont += 1
    print(dict_clientes)
    return render(request, 'VisualizacoesBD/visual-clientes.html', {'clientes': dict_clientes})

@login_required
def visual_produtos_view(request):
    produtos = Produto.objects.all()
    dict_produtos = {}
    cont = 0
    for produto in produtos:
        dict_produtos[cont] = produto
        cont += 1
    return render(request, 'VisualizacoesBD/visual-produtos.html', {'produtos': dict_produtos})

@login_required
def visual_vendas_view(request):
    vendas = Venda.objects.all()
    dict_vendas = {}
    cont = 0
    for venda in vendas:
        dict_vendas[cont] = venda
        cont += 1
    return render(request, 'VisualizacoesBD/visual-vendas.html', {'vendas': dict_vendas})

@login_required
def visual_despesas_view(request):
    despesas = Despesa.objects.all()
    dict_despesas = {}
    cont = 0
    for despesa in despesas:
        dict_despesas[cont] = despesa
        cont += 1
    return render(request, 'VisualizacoesBD/visual-despesas.html', {'despesas': despesas})
