from django.contrib import admin
from django.urls import path

from apps.conferencias.views import mostrarConferencias

app_name = 'conferencia'

urlpatterns = [
    path("",mostrarConferencias.as_view(),name='index'),
]