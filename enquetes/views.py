from django.shortcuts import render

def home(request):
    return render(request, 'enquetes/pages/home.html')
