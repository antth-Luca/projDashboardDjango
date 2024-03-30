from django.contrib import admin
from .models import Cliente, Vendedor, Produto, Venda, Despesa

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Despesa)