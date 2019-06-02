from django.contrib import admin
from django.urls import path

from apps.conferencias.views import mostrarConferencias,myConferencias
from django.contrib.auth.decorators import login_required
app_name = 'conferencia'

urlpatterns = [
    path("",login_required(mostrarConferencias.as_view()),name='index'),
    path("home",login_required(myConferencias.as_view()),name='home')
]