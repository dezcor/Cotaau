from django.contrib import admin

# Register your models here.
from apps.estudiantes.models import Estudiante,Carrera,Sexo

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('NUA','user','semestre','carrera','sexo')
    list_filter = ('carrera','sexo',)
    search_fields = ('NUA',)


admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Carrera)
admin.site.register(Sexo)