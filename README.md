# django-basico-udemy

12/11/2023

Aula 23 - configurando settings (basico):

Templates = [
    'DIR': ['templates']
]

LANGUAGE_CODE = 'pt-br'

------------------------------------------------------------------------------------------------------------

aula 24 - configurando arquivo views.py

criado em views a função index, para pagina incial do django:

def index(request):
    return render(request, 'index.html')

------------------------------------------------------------------------------------------------------------

aula 25 - adicionando as rotas aos arquivos em URL

importando a views da aplicação:

from udemy1.views import index

logo em seguida:

path('', index), --> adicionar em urlpatterns

quando alguem acessar a parte de arquivos do admin, faz isso:

from django.urls import path, ''include'' -- >importar esse include!

path('', include('aplicação.urls')),

e na aplicação cria o arquivo 'urls.py'

from django.urls import path
from .views import index --> Importa esses dois ai

urlpatterns = [
    path('', index),
    
]

(qualquer coisa rever essa aula!)

------------------------------------------------------------------------------------------------------------

aula 26 - Templates no django

Cria na aplicação a pasta -> templates

cria arquivo index e escreve o que quiser, para a página inicial do Django!




