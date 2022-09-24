from django.db import models
from . historia_clinica import Historia_clinica
from .login import login
from .medico import Medico

class Paciente(models.Model):
     
 cedula_pac=models.CharField (primary_key=True)
 nombre = models.CharField (max_length=20)
 apellido_1=models.CharField (max_length=20)
 apellido_2=models.CharField (max_length=20)
 fecha_nto=models.CharField (max_length=20)
 direccion_pac=models.CharField (max_length=20)
 cedula_med=models.CharField (max_length=20)
 cedula_enfe=models.CharField (max_length=20)
 numtel_pac=models.CharField (max_length=10)
 cedula_med=  models.ForeignKey (Medico, related_name='paciente',on_delete=models.CASCADE)
 Historia_clinica=models.ForeignKey (Historia_clinica, related_name='Historia_clinica',on_delete=models.CASCADE)
 login =models.ForeignKey (login.related_model'login',on_delete=models.cascade) 
