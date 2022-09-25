from django.db import models

from apphos.models.Enfermero import Enfermero
from apphos.models.Familiar import Familiar
from apphos.models.Historia_clinica import Historia_clinica
from apphos.models.Medico import Medico
from apphos.models.Login import login
from apphos.models.Historia_clinica import Historia_clinica
from apphos.models.Auxiliar import Auxiliar 

class Paciente(models.Model):
     
 cedula_pac=models.CharField (primary_key=True)
 nombre = models.CharField (max_length=20)
 apellido_1=models.CharField (max_length=20)
 apellido_2=models.CharField (max_length=20)
 fecha_nto=models.CharField (max_length=20)
 direccion_pac=models.CharField (max_length=20)
 ciudad=models.CharField (max_length=20)
 cedula_med=models.CharField (max_length=20)
 cedula_enfe=models.CharField (max_length=20)
 numtel_pac=models.CharField (max_length=10)
 cedula_med=  models.ForeignKey (Medico, related_name='paciente',on_delete=models.CASCADE)
 cedula_enfe=  models.ForeignKey (Enfermero, related_name='enfermero',on_delete=models.CASCADE)
 Historia_clinica=models.ForeignKey (Historia_clinica, related_name='Historia_clinica',on_delete=models.CASCADE)
 login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
 Auxiliar =models.ForeignKey (Auxiliar, related_name='Auxiliar',on_delete=models.CASCADE)
 Medico =models.ForeignKey (Medico, related_name='Medico',on_delete=models.CASCADE)
 Enfermero =models.ForeignKey (Enfermero, related_name='Enfermero',on_delete=models.CASCADE)
 Familiar =models.ForeignKey (Familiar, related_name='Familiar',on_delete=models.CASCADE) 
	
