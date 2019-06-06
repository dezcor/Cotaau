"""cotaau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from apps.estudiantes.views import Login
from apps.conferencias.views import RegistroConferencias, conferencia_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/',include("apps.estudiantes.urls")),
    path("ponentes/",include("apps.ponentes.urls")),
    path("logout/",LogoutView.as_view(),name = 'logout'),
    path("conferencias/",include('apps.conferencias.urls')),
    path("accounts/login/",Login.as_view(),{'template_name':'index.html'},name='login'),
    path("conferencias/Registro/",RegistroConferencias.as_view(),{'template_name':'conferencia_registro.html'},name='Registro'),
    path("conferencias/info",conferencia_view,{"template_name":'conferencia_info.html'},name="info"),
    path("accounts/password_reset",PasswordResetView.as_view(),name='password_reset'),
    path("accounts/password_reset/done/",PasswordResetDoneView.as_view(),name= 'password_reset_done'),
    path("accounts/reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name= 'password_reset_confirm'),
    path("accounts/reset/done/",PasswordResetCompleteView.as_view(),name= 'password_reset_complete'),
    path('main/', TemplateView.as_view(template_name="principal/main.html"))

]
