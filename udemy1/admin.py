from django.contrib import admin
from .models import Produto, Clientes

# Verificar isso o do porque não aparecer no sistema administrativo.
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClientesAdmin(admin.ModelAdmin):
    list_display = {'nome', 'sobrenome', 'email'}

admin.site.register(Produto)
admin.site.register(Clientes) 