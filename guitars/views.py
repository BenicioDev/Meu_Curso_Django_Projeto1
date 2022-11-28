from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('PÁGINA HOME')


def contato(request):
    return HttpResponse('Contatos da página')


def sobre(request):
    return HttpResponse('Sobre nós')
