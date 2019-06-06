from django.shortcuts import render
from apps.conferencias.models import Conferencia,Registro
from apps.estudiantes.models import Estudiante
from django.views.generic import ListView,View
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import Http404

from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.views import LoginView
from django.views.generic import ListView,CreateView,UpdateView
from apps.conferencias.models import Conferencia
from apps.conferencias.models import Registro 

from apps.conferencias.forms import ConferenciaFrom,UpdateEntradaFrom



class RegistroConferencias(CreateView):
    model = Conferencia
    template_name = 'conferencias/conferencia_registro.html'
    form_class = ConferenciaFrom
    success_url = reverse_lazy("Registro")
  

            


class mostrarConferencias(ListView):
    model = Conferencia
    template_name = 'conferencias/conferencia_list.html'
    paginate_by = 10

class myConferencias(ListView):
    model = Conferencia
    template_name = 'conferencias/myconferencia_list.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            estudiante = Estudiante.objects.get(user = self.request.user)
            registros = Registro.objects.filter(NUA = estudiante.NUA)
        except Estudiante.DoesNotExist:
            return []
        except Registro.DoesNotExist:
            return []
        return registros
        
class UpdateReistroEntradaView(UpdateView):
    model =  Registro
    template_name = 'conferencias/Conferencia_Update_Entrada.html'
    success_url = reverse_lazy("conferencia:index")
    form_class = UpdateEntradaFrom

def conferencia_view(request):
    conferencia_list = Conferencia.objects.all()
    context = {'conferencia_list': conferencia_list}
    return render(request, 'conferencia_info/conferencia_info.html', context)

