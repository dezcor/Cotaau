from django.db import models
from apps.estudiantes.models import Sexo

# Create your models here.
from apps.estudiantes.models import Sexo

class Ponente(models.Model):
    Nombre = models.CharField(max_length=50)
    Trayectoria = models.TextField()
    edad = models.IntegerField()
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)

    def __str__(self):
        return "{} | {}".format(self.Nombre,self.edad)