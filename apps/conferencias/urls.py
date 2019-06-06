from django.contrib import admin
from django.urls import path

from apps.conferencias.views import mostrarConferencias,myConferencias,SalidaView,UpdateReistroEntradaView as UREView
from apps.conferencias.views import conferencia_view
from apps.conferencias.views import RegistroConferencias, conferencia_view
from django.contrib.auth.decorators import login_required
app_name = 'conferencia'


urlpatterns = [
    path("",login_required(mostrarConferencias.as_view()),name='index'),
    path("home",login_required(myConferencias.as_view()),name='home'),
    path("Registro/edit/<int:pk>",login_required(UREView.as_view()),name='entrada'),
    path("Registro/<int:conferencia_id>/crear",login_required(RegistroConferencias.as_view()),name='Registro'),
    path("Salida/edit/<int:pk>",login_required(SalidaView.as_view()),name='Salida'),
    path("info/<int:id>",login_required(conferencia_view),name="info"),
]