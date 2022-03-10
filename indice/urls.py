from django.urls import path
from .views import indice, plantilla

urlpatterns = [
  path('', indice, name='indice'),
  path('plantilla/', plantilla, name='plantilla')
]