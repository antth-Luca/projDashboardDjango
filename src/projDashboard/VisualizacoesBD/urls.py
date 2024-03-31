from django.urls import path
from .views import visual_clientes_view, visual_produtos_view, visual_vendas_view, visual_despesas_view

urlpatterns = [
    path('visualizar-clientes/', visual_clientes_view, name='VisualClientes'),
    path('visualizar-produtos/', visual_produtos_view, name='VisualProdutos'),
    path('visualizar-vendas/', visual_vendas_view, name='VisualVendas'),
    path('visualizar-despesas/', visual_despesas_view, name='VisualDespesas'),
]