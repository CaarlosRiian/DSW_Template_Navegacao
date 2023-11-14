from django.shortcuts import render

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def produto(request, pk):
    produto = Produto.objects.get(id=pk)
    context = {
        'produto': produto
    }
    return render(request, 'produto.html', context)

