from django.contrib import admin

# Register your models here.
from apps.conferencias.models import Conferencia,Auditorio,Tipo

admin.site.register(Conferencia)
admin.site.register(Auditorio)
admin.site.register(Tipo)