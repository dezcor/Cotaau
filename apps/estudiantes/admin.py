from django.contrib import admin

# Register your models here.
from apps.estudiantes.models import Estudiante,Carrera,Sexo

admin.site.register(Estudiante)
admin.site.register(Carrera)
admin.site.register(Sexo)