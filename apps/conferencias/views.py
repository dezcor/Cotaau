from django.shortcuts import render
from apps.conferencias.models import Conferencia,Registro
from apps.estudiantes.models import Estudiante
from django.views.generic import ListView,View
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import Http404
from datetime import time,datetime
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.views import LoginView
from django.views.generic import ListView,CreateView,UpdateView
from apps.conferencias.models import Conferencia
from apps.conferencias.models import Registro 

from apps.conferencias.forms import ConferenciaFrom,UpdateEntradaFrom,UpdateSalidaFrom



class RegistroConferencias(CreateView):
    model = Registro
    template_name = 'conferencias/conferencia_registro.html'
    form_class = ConferenciaFrom
    success_url = reverse_lazy("conferencia:home")   
    extra_context = 'mensaje_error'
    
    def get(self, request, *args, **kwargs):
        conferencia = kwargs['conferencia_id']
        if conferencia:
            # Intentamos recuperar ese usario desde la DB 
            conferencia = Conferencia.objects.get(id=conferencia)
            # Ese get puede fallar, deberías capturar la excepción
            # Inicializamos el form con ese usuario ya cargado
            user = self.request.user
            alumno = user.estudiante
            initial= {'NUA': alumno.NUA }
            initial['conferencia'] = conferencia
            form = self.form_class(initial=initial)

            try:
                e = Registro.objects.get(NUA = alumno.NUA, conferencia = conferencia)
                context = {"error_message":'Ya te as registrado'}
            except Registro.DoesNotExist:
                context = {}
        else:
            # Si no especificaron usuario en el request
            # mostramos el form vacio
            form = self.form_class()
        #context = self.get_context_data(**kwargs)
        context['form'] =form
        return render(request, self.template_name, context)         

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

    def get(self, request, *args, **kwargs):
        registro_id = kwargs['pk']
        if registro_id:
            # Intentamos recuperar ese usario desde la DB 
            conferencia = self.model.objects.get(id=registro_id)
            # Ese get puede fallar, deberías capturar la excepción
            # Inicializamos el form con ese usuario ya cargado
            user = self.request.user
            alumno = user.estudiante
            initial= {'NUA': conferencia.NUA }
            hora = datetime.now()
            hora = time(hora.hour,hora.minute)
            res = conferencia.conferencia.valida_fecha()
            if res==2:
                context = {"hora_novalida":"Ya termino la conferencia"}
            if res==1:
                context = {"hora_novalida":"Aun no a comensado la conferencia"}
            if res == 0:
                context = {}
            if conferencia.Hora_Entrada is None:
                initial['Hora_Entrada']= hora
            else:
                initial['Hora_Entrada']= conferencia.Hora_Entrada
                context = {"hora_novalida":"Ya resgistraste tu hora de Entrada"}
        else:
            # Si no especificaron usuario en el request
            # mostramos el form vacio
            form = self.form_class()
        context['form'] = form
        return render(request, self.template_name, context)         

def conferencia_view(request,id):
    conferencia_list = get_object_or_404(Conferencia,pk=id)
    context = {'conferencia': conferencia_list}
    return render(request, 'conferencia_info/conferencia_info.html', context)




       
class SalidaView(UpdateView):
    model =  Registro
    template_name = 'conferencias/conferencia_Salida.html'
    success_url = reverse_lazy("conferencia:index")
    form_class = UpdateSalidaFrom

    def get(self, request, *args, **kwargs):
        registro_id = kwargs['pk']
        if registro_id:
            # Intentamos recuperar ese usario desde la DB 
            conferencia = self.model.objects.get(id=registro_id)
            # Ese get puede fallar, deberías capturar la excepción
            # Inicializamos el form con ese usuario ya cargado
            user = self.request.user
            alumno = user.estudiante
            initial= {'NUA': conferencia.NUA }
            hora = datetime.now()
            hora = time(hora.hour,hora.minute)

            res = conferencia.conferencia.valida_fecha()
            if res==2:
                context = {"hora_novalida":"Ya termino la conferencia"}
            if res==1:
                context = {"hora_novalida":"Aun no a comensado la conferencia"}
            if res == 0:
                context = {}
            if conferencia.Hora_Salida is None:
                initial['Hora_Salida'] = hora
                initial['Hora_Entrada']= conferencia.Hora_Entrada
            else:
                initial['Hora_Salida'] = conferencia.Hora_Salida
                initial['Hora_Entrada']= conferencia.Hora_Entrada
                context = {"hora_novalida":"Ya resgistraste tu hora de Salida"}
            initial['conferencia'] = conferencia.conferencia
            form = self.form_class(initial=initial)
            
        else:
            # Si no especificaron usuario en el request
            # mostramos el form vacio
            form = self.form_class()
        context['form'] = form
        return render(request, self.template_name, context)         