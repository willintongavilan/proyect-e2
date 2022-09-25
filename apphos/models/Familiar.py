from django.db import models
from .Login import Login
from .Paciente import Paciente

class Familiar(models.model):
    cedula_fam=models.CharField (primary_key="true")
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    celular=models.CharField (max_length=10)
    email=models.CharField (max_length=50)
    direccion=models.CharField (max_length=30)
    
	
