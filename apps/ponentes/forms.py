from django import forms
from apps.ponentes.models import Ponente

class PonentesForm(forms.ModelForm):
    
    class Meta:
        model = Ponente

        fields = [
            'Nombre',
            'edad',
            'sexo',
            'Trayectoria',
        ]
        label = {
            'Nombre': 'Nombre',
            'edad': 'Edad',
            'sexo': 'Sexo',
            'Trayectoria': 'Trayectoria',
        }
        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'Trayectoria': forms.Textarea(attrs={'class':'form-control'}),
        }
