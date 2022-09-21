from django.db import models

class Enfermero(models.model):
    Cedula_enfe=models.CharField (primary_key=true) (max_length=10)
	Nombre=models.CharField (max_length=20)
	Apellido_1=models.CharField (max_length=20)
	Apellido_2=models.CharField (max_length=20)
	login =models.ForeignKey (login.related_model'login',on_delete=models.cascade)
	
