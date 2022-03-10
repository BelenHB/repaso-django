from django.contrib import admin

from profesionales.models import Cerrajero, Futbolista, Profesional

# Register your models here.
admin.site.register(Profesional)

admin.site.register(Cerrajero)

admin.site.register(Futbolista)