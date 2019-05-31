from django.shortcuts import render
from apps.conferencias.models import Conferencia
from django.views.generic import ListView

# Create your views here.


class mostrarConferencias(ListView):
    model = Conferencia
    template_name = 'conferencias/conferencia_list.html'