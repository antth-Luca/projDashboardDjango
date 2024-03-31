from django import forms
from Central.models import Cliente, Produto, Venda, Despesa

class RegistClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome']


class RegistProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']


class RegistVendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['vendedor', 'cliente', 'produto', 'quantidade']

class RegistDespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['valor']
