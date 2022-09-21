from django.db import models

class Medico(models.model):
    cedula_med=models.CharField (primary_key=true)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20) 
    login =models.ForeignKey (login.related_model'login',on_delete=models.cascade)	
	
    
	
