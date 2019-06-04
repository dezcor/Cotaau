from django import forms

from apps.conferencias.models import Conferencia,Registro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ConferenciaFrom(forms.ModelForm):
 
    class Meta:
            model= Registro
            
            fields = [
                'NUA',
                'Hora_Entrada',
                'Hora_Salida',
                'conferencia',
                
             
            ]
            labels = {
                'NUA': 'NUA',
                'Hora_Entrada': 'Hora_Entrada',
                'Hora_Salida': 'Hora_Salida',
                'conferencia':'Conferencia',
            }

            widgets = {
                'NUA':          forms.NumberInput(attrs={'class':'form-control'}),
                'Hora_Entrada': forms.TimeInput(attrs={'class':'form-control'}),
                'Hora_Salida':  forms.TimeInput(attrs={'class':'form-control'}),
                'conferencia':  forms.Select(attrs={'class':'form-control'}),
                
            }


   