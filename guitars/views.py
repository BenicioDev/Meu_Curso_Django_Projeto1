from django.http import HttpResponse
from django.shortcuts import render

# Função Render renderiza a Pagina HTML na pasta Templates


def home(request):
    # Return solicita o render que recebe um request com o nome do Arquivo
    # HTML django, no caso 'home.html'
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('Contatos da página')


def sobre(request):
    return HttpResponse('Sobre nós')
