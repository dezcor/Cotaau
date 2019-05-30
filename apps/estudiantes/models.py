from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carrera(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Sexo(models.Model):
   sexo = models.CharField(max_length=10)

   def __str__(self):
       return self.sexo

class Estudiante(models.Model):
    NUA = models.IntegerField(unique=True,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    semestre = models.IntegerField()
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.NUA)+ self.user.first_name