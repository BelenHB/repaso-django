from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def indice(request):
  return HttpResponse('<h1>Bienvenidos a mi página de Django</h1>')

def plantilla(request):
  template = loader.get_template('plantilla.html')
  
  datos = {
    'lista':['primero', 'segundo', 'tercero'],
    'nombre': 'Juan',
    'condicion': True
  }
  
  plantilla_generada = template.render(datos)
  
  return HttpResponse(plantilla_generada)