from django.contrib import admin
from django.urls import path

from apps.conferencias.views import mostrarConferencias,myConferencias,UpdateReistroEntradaView as UREView
from apps.conferencias.views import conferencia_view
from apps.conferencias.views import RegistroConferencias, conferencia_view
from django.contrib.auth.decorators import login_required
app_name = 'conferencia'


urlpatterns = [
    path("",login_required(mostrarConferencias.as_view()),name='index'),
    path("home",login_required(myConferencias.as_view()),name='home'),
    path("Registro/edit/<int:pk>",UREView.as_view(),name='entrada'),
    path("Registro/",RegistroConferencias.as_view(),{'template_name':'conferencia_registro.html'},name='Registro'),
    path("info/<int:id>",conferencia_view,name="info"),
]