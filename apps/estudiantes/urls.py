from django.contrib import admin
from django.urls import path

from apps.estudiantes.views import CrearUsuario

app_name = 'estudiante'

urlpatterns = [
    path("resgistrar",CrearUsuario.as_view(),name='registro'),
]