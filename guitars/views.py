from django.shortcuts import render

# Função Render renderiza a Pagina HTML na pasta Templates


def home(request):
    # Return solicita o render que recebe um request com o nome do Arquivo
    # HTML django, no caso 'home.html'
    return render(request, 'pages/home.html')


def guitars(request, id):
    return render(request, 'pages/guitars-view.html')
