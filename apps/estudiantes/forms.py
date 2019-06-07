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
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Username",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'first_name':forms.TextInput(attrs={'class':'form-control',"placeholder":"Nombre",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'email':forms.EmailInput(attrs={'class':'form-control',"placeholder":"Email",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'last_name':forms.TextInput(attrs={'class':'form-control',"placeholder":"Apellidos",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
        }
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
            'NUA': forms.NumberInput(attrs={'class':'form-control',"placeholder":"NUA",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'semestre':forms.NumberInput(attrs={'class':'form-control',"placeholder":"Semestre",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'carrera':forms.Select(attrs={'class':'form-control','aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
            'sexo':forms.Select(attrs={'class':'form-control','aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
        }

class UpdateRegsForm(forms.ModelForm):
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
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Username",'aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'first_name':forms.TextInput(attrs={'class':'form-control',"placeholder":"Nombre",'aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'email':forms.EmailInput(attrs={'class':'form-control',"placeholder":"Email",'aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'last_name':forms.TextInput(attrs={'class':'form-control',"placeholder":"Apellidos",'aria-describedby':"sizing-addon1",'required style':"width:700px;height:50px"}),
        }

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
            'NUA': forms.NumberInput(attrs={'class':'form-control',"placeholder":"NUA",'aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'semestre':forms.NumberInput(attrs={'class':'form-control',"placeholder":"Semestre",'aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'carrera':forms.Select(attrs={'class':'form-control','aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
            'sexo':forms.Select(attrs={'class':'form-control','aria-describedby':"sizing-addon1",'required style':"width:auto;height:50px"}),
        }
