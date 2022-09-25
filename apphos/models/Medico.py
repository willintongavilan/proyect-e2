from django.db import models
from . Login import login
from . Historia_clinica import Historia_clinica

class Medico(models.model):
    cedula_med=models.CharField (primary_key=True)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20) 
    numtel_med=models.CharField (max_length=10)
    Historia_clinica=models.ForeignKey (Historia_clinica, related_name='Historia_clinica',on_delete=models.CASCADE)
    login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
	
