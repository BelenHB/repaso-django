from django.db import models

# Create your models here.

class Profesional(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)

class Cerrajero(Profesional):
  # nombre = models.CharField(max_length=50)
  # apellido = models.CharField(max_length=50)
  desempleado = models.BooleanField()
  
  tel = models.IntegerField()
  
class Futbolista(Profesional):
  # nombre = models.CharField(max_length=20)
  # apellido = models.CharField(max_length=20)
  club_futbol = models.CharField(max_length=30)
  
