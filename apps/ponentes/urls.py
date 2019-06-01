from django.contrib import admin
from django.urls import path

from apps.ponentes.views import ponentes_list
from django.contrib.auth.decorators import login_required
app_name = 'ponentes'
urlpatterns = [
    path("",login_required(ponentes_list.as_view()),name='index'),
]