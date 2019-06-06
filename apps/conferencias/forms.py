from django import forms

from apps.conferencias.models import Conferencia,Registro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ConferenciaFrom(forms.ModelForm):
 
    class Meta:
        model= Registro
        
        fields = [
            'NUA',
            # 'Hora_Entrada',
            # 'Hora_Salida',
            'conferencia',   
        ]
        labels = {
            'NUA': 'NUA',
            # 'Hora_Entrada': 'Hora Entrada',
            # 'Hora_Salida': 'Hora Salida',
            'conferencia':'Conferencia',
        }

        widgets = {
            'NUA':          forms.NumberInput(attrs={'class':'form-control',"name":"NUA","placeholder":"NUA","aria-describedby":"sizing-addon1","required":"required"}),
            # 'Hora_Entrada': forms.TimeInput(attrs={'class':'form-control'}),
            # 'Hora_Salida':  forms.TimeInput(attrs={'class':'form-control'}),
            'conferencia':  forms.Select(attrs={'class':'form-control'}),
            
        }

class UpdateEntradaFrom(forms.ModelForm):
    
    class Meta:
        model = Registro
        fields = [
            'NUA',
            'Hora_Entrada',
            'conferencia',
        ]
        labels = {
            'NUA': 'NUA',
            'Hora_Entrada': 'Hora Entrada',
            'conferencia':'Conferencia',
        }

        widgets = {
            'NUA':          forms.NumberInput(attrs={'class':'form-control',"readonly":"readonly"}),
            'Hora_Entrada': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'conferencia':  forms.Select(attrs={'class':'form-control'}),
        }
