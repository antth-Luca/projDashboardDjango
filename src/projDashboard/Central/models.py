from django.db import models
from datetime import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cadastro_em = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.vendedor} vendeu {self.produto} em um total de R$ {self.total} para {self.cliente} em {f"{self.data.day}/{self.data.month}/{self.data.year}"}'


class Despesa(models.Model):
    valor = models.FloatField()
    data = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'Houve uma despesa de R$ {self.valor} em {f"{self.data.day}/{self.data.month}/{self.data.year}"}'
