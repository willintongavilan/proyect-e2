from django.db import models
from apphos.models.Login import login

from apphos.models.Auxiliar import Auxiliar 



class Medico(models.Model):
    cedula_med=models.CharField (primary_key=True)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20) 
    numtel_med=models.CharField (max_length=10)

    login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
    Auxiliar =models.ForeignKey (Auxiliar, related_name='Auxiliar', on_delete=models.CASCADE)
  
    