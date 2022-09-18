from django.db import models

class Medico(models.model):
    Cedula_med=models.CharField (primary_key=true)
	Nombre=models.CharField (max_length=20)
	Apellido_1=models.CharField (max_length=20)
    Apellido_2=models.CharField (max_length=20)
    
	
