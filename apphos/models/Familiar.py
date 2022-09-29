from django.db import models
from apphos.models.Login import login
from apphos.models.Paciente import Paciente
from apphos.models.Auxiliar import Auxiliar

class Familiar(models.Model):
    cedula_fam=models.CharField (primary_key=True, max_length=40)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    celular=models.CharField (max_length=10)
    email=models.CharField (max_length=50)
    direccion=models.CharField (max_length=30)
    cedula_paciente=models.ForeignKey(Paciente,related_name='Familiar', on_delete=models.CASCADE)
    login=models.ForeignKey(login, related_name='Familiar', on_delete=models.CASCADE)
    Auxiliar = models.ForeignKey (Auxiliar, related_name='Familiar', on_delete=models.CASCADE)
    
    
	
