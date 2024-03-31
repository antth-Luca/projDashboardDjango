from django.urls import path
from .views import regist_cliente_view, regist_produto_view, regist_venda_view, regist_despesa_view

urlpatterns = [
    path('registrar-cliente/', regist_cliente_view, name='RegistCliente'),
    path('registrar-produto/', regist_produto_view, name='RegistProduto'),
    path('registrar-venda/', regist_venda_view, name='RegistVenda'),
    path('registrar-despesa/', regist_despesa_view, name='RegistDespesa'),
]