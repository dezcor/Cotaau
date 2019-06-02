from django.contrib import admin

# Register your models here.
from apps.conferencias.models import Conferencia,Auditorio,Tipo,Registro

class ConferenciaAdmin(admin.ModelAdmin):
    ordering = ("Fecha",)
    list_display = ('id_aud','Titulo','ponente','Fecha','Hora_ini')
    list_filter = ('Fecha','id_aud')
    search_fields = ('Titulo',)

class RegistroAdmin(admin.ModelAdmin):
    fields = ('NUA', 'conferencia')

admin.site.register(Conferencia,ConferenciaAdmin)
admin.site.register(Auditorio)
admin.site.register(Registro,RegistroAdmin)
admin.site.register(Tipo)