from django.db import models
from proyect-e2.apphos.models.Historia_clinica import Historia_clinica

class paciente(models.model):
     
 cedula_pac=models.CharField (primary_key=True)
 nombre = models.CharField (max_length=20)
 apellido_1=models.CharField (max_length=20)
 apellido_2=models.CharField (max_length=20)
 fecha_nto=models.CharField (max_length=20)
 direccion_pac=models.CharField (max_length=20)
 cedula_med=models.CharField (max_length=20)
 cedula_enfe=models.CharField (max_length=20)
 cedula_med=  models.ForeignKey (cedula_med.related_model'medico',on_delete=models.cascade)
 Historia_clinica=models.ForeignKey (Historia_clinica.related_model'Historia_clinica',on_delete=models.cascade)
