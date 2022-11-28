from django.urls import path

from guitars.views import contato, home, sobre

urlpatterns = [
    path('', home),  # home
    path('contato/', contato),  # contatos
    path('sobre/', sobre)  # sobre
]
