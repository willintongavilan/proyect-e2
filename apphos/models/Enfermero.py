from django.db import models

class Enfermero(models.model):
    cedula_enfe=models.CharField (primary_key=true) (max_length=10)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    numtel_enfe=models.CharField (max_length=10)
    login =models.ForeignKey (login.related_model'login',on_delete=models.cascade)
	
	
