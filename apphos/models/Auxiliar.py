from django.db import models
from apphos.models.Login import login

class Auxiliar(models.Model):
    cedula_aux=models.CharField (primary_key=True)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20) 
    numtel_aux=models.CharField (max_length=10)
    login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
	
