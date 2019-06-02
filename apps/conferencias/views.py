from django.shortcuts import render
from apps.conferencias.models import Conferencia,Registro
from apps.estudiantes.models import Estudiante
from django.views.generic import ListView,View
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import Http404

# Create your views here.


class mostrarConferencias(ListView):
    model = Conferencia
    template_name = 'conferencias/conferencia_list.html'
    paginate_by = 10

class myConferencias(ListView):
    model = Conferencia
    template_name = 'conferencias/conferencia_list.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            estudiante = Estudiante.objects.get(user = self.request.user)
            registros = Registro.objects.filter(NUA = estudiante.NUA)
        except Estudiante.DoesNotExist:
            return []
        except Registro.DoesNotExist:
            return []
        return [cons.conferencia for cons in registros]
        
class ConferenciaIndex():
    pass