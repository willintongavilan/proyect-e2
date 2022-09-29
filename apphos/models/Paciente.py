from django.db import models
from .Enfermero import Enfermero


from apphos.models.Medico import Medico
from apphos.models.Login import login

from apphos.models.Auxiliar import Auxiliar 

class Paciente(models.Model):
     
 cedula_pac=models.CharField (primary_key=True,max_length=40)
 nombre = models.CharField (max_length=20)
 apellido_1=models.CharField (max_length=20)
 apellido_2=models.CharField (max_length=20)
 fecha_nto=models.CharField (max_length=20)
 direccion_pac=models.CharField (max_length=20)
 ciudad=models.CharField (max_length=20)
 numtel_pac=models.CharField (max_length=10)
 cedula_med=  models.ForeignKey (Medico, related_name='Paciente',on_delete=models.CASCADE)

 login =models.ForeignKey (login, related_name='Paciente',on_delete=models.CASCADE)
 Auxiliar =models.ForeignKey (Auxiliar, related_name='Paciente',on_delete=models.CASCADE)
 
 Enfermero =models.ForeignKey (Enfermero, related_name='Paciente',on_delete=models.CASCADE)

	
