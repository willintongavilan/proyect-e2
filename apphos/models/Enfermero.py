from django.db import models

from apphos.models.Auxiliar import Auxiliar
from apphos.models.Login import login




class Enfermero(models.Model):
    cedula_enfe=models.CharField (primary_key=True,max_length=40)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    numtel_enfe=models.CharField (max_length=10)

    login =models.ForeignKey (login, related_name='Enfermero',on_delete=models.CASCADE)

    Auxiliar = models.ForeignKey (Auxiliar, related_name='Enfermero', on_delete=models.CASCADE)

    
