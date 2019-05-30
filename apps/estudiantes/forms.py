from django import forms

from apps.estudiantes.models import Estudiante
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = [
            {'username': 'Nombre de Usuario'},
            {'first_name': 'Nombre'},
            {'last_name': 'Apellidos'},
            {'email': 'Correo'},
        ]
    
class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = [
            'NUA',
            'semestre',
            'carrera',
            'sexo',
        ]

        labels = {
            'NUA': 'NUA',
            'semestre': 'Semestre',
            'carrera': 'Carrera',
            'sexo': 'Sexo',
        }

        widgets = {
            'NUA': forms.NumberInput(attrs={'class':'form-control'}),
            'semestre':forms.NumberInput(attrs={'class':'form-control'}),
            'carrera':forms.Select(attrs={'class':'form-control'}),
            'sexo':forms.Select(attrs={'class':'form-control'}),
        }