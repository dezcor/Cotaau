from django.db import models
from apps.ponentes.models import Ponente
# Create your models here.
from apps.estudiantes.models import Estudiante

class Auditorio(models.Model):
    Nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.Nombre
class Tipo(models.Model):
    Nombre = models.CharField(max_length=20) 

    def __str__(self):
        return self.Nombre
class Conferencia(models.Model):
    id_aud = models.ForeignKey(Auditorio,on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=30)
    explicacion = models.TextField()
    Fecha = models.DateField()
    Hora_ini = models.TimeField()
    Hora_fin = models.TimeField()
    tipo =  models.ForeignKey(Tipo,on_delete = models.CASCADE)
    ponente = models.ForeignKey(Ponente,on_delete = models.CASCADE)

    def __str__(self):
        return "Auditorio: {}, Fecha: {}, Esponente: {} Titulo: {}".format(self.id_aud.Nombre,self.Fecha,self.ponente.Nombre,self.Titulo)

class Registro(models.Model):
    NUA = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    Hora_Entrada =  models.TimeField(null=True)
    Hora_Salida = models.TimeField(null=True)
    conferencia = models.ForeignKey(Conferencia,on_delete=models.CASCADE)

    def __str__(self):
        return self.NUA.user.first_name + ' ' + str(self.Hora_Entrada) +' ' + str(self.Hora_Salida)+' '+str(self.conferencia)