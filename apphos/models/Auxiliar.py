from django.db import models

class Auxiliar(models.model):
    cedula_aux=models.CharField (primary_key=true)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20) 
    numtel_aux=models.CharField (max_length=10)
    login =models.ForeignKey (login.related_model'login',on_delete=models.cascade)	
