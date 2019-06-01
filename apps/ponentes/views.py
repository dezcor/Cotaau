from django.shortcuts import render,redirect

# Create your views here.
from apps.ponentes.forms import PonentesForm
from apps.ponentes.models import Ponente
from django.views.generic import ListView

class ponentes_list(ListView):
    model = Ponente
    template_name = 'ponentes/index.html'
    paginate_by = 10
