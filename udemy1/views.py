from django.shortcuts import render

def index(request):
    testando = {
        'kalebe': 'vai que né kkkkkkk'
    }
    return render(request, 'index.html', testando)
