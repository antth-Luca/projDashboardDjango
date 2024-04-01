from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from Central.models import Cliente, Produto, Venda, Despesa, Vendedor

class RegistClienteForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNome', 'placeholder': 'Digite o nome do cliente'}),
        max_length=150, required=True
    )

    class Meta:
        model = Cliente
        fields = ['nome']


class RegistProdutoForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputNome', 'placeholder': 'Digite o nome do produto'}),
        max_length=150, required=True
    )
    preco = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputPreco', 'placeholder': 'Digite o preço'}),
        required=True
    )

    class Meta:
        model = Produto
        fields = ['nome', 'preco']


class RegistVendaForm(forms.Form):
    vendedor = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'inputVendedor', 'placeholder': 'Escolha o vendedor'}),
        required=True
    )
    cliente = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'inputCliente', 'placeholder': 'Escolha o cliente'}),
        required=True
    )
    produto = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'inputProduto', 'placeholder': 'Escolha o produto'}),
        required=True
    )
    quantidade = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputQuant', 'placeholder': 'Digite a quantidade de produtos'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].choices = [('', 'Escolha o vendedor')] + [(v.nome, v.nome) for v in Vendedor.objects.all()]

        self.fields['cliente'].choices = [('', 'Escolha o cliente')] + [(c.nome, c.nome) for c in Cliente.objects.all()]

        self.fields['produto'].choices = [('', 'Escolha o produto')] + [(p.nome, p.nome) for p in Produto.objects.all()]


class RegistDespesaForm(forms.ModelForm):
    valor = forms.FloatField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputValor', 'placeholder': 'Digite o valor'}),
        required=True
    )

    class Meta:
        model = Despesa
        fields = ['valor']
