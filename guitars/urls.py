from django.urls import path

from guitars.views import home

urlpatterns = [
    path('', home),  # home
]
