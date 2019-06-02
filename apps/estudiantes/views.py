from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView,CreateView
from apps.estudiantes.models import Estudiante
from django.contrib.auth.models import User
from apps.estudiantes.forms import EstudianteForm, RegistroForm
from django.contrib.auth.views import LoginView

class Login(LoginView):
    success_url = reverse_lazy("conferencia:index")

class CrearUsuario(CreateView):
    model = Estudiante
    template_name = 'estudiantes/Estudiante_form2.html'
    form_class = EstudianteForm
    second_form_class = RegistroForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super(CrearUsuario,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(self.request.POST)
        form2 = self.second_form_class(self.request.POST)
        if form.is_valid() and form2.is_valid():
            estudiante = form.save(commit=False)
            estudiante.user = form2.save()
            estudiante.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))