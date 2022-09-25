from django.db import models
from apphos.models.Login import login
from apphos.models.Paciente import Paciente
from apphos.models.Auxiliar import Auxiliar

class Familiar(models.model):
    cedula_fam=models.CharField (primary_key="true")
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    celular=models.CharField (max_length=10)
    email=models.CharField (max_length=50)
    direccion=models.CharField (max_length=30)
    login=models.ForeignKey(login, related_name='login', on_delete=models.CASCADE)
    Auxiliar = models.ForeignKey (Auxiliar, related_name='Auxiliar', on_delete=models.CASCADE)
    Paciente = models.ForeignKey (Paciente, related_name='Paciente', on_delete=models.CASCADE)
    
	
