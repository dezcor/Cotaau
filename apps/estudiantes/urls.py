from django.contrib import admin
from django.urls import path

from apps.estudiantes.views import CrearUsuario, UpdateUsuario
from django.contrib.auth.decorators import login_required
app_name = 'estudiante'

urlpatterns = [
    path("registrar",CrearUsuario.as_view(),name='registro'),
    path("editar/<int:pk>",login_required(UpdateUsuario.as_view()),name = 'editar'),
]