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

class UpdateRegsForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(UpdateRegsForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UpdateEstudenFrom(forms.ModelForm):
    NUA = forms.IntegerField(required=True)
    semestre = forms.IntegerField(required=True)
    carrera = forms.Select()
    sexo = forms.Select()
    class Meta:
        model = Estudiante
        fields = [
            'NUA',
            'semestre',
            'carrera',
            'sexo',
        ]
