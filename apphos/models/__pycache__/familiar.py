from django.db import models

class Familiar(models.model):
    Cedula_fam=models.CharField (primary_key=true)
	Nombre=models.CharField (max_length=20)
	Apellido_1=models.CharField (max_length=20)
	Apellido_2=models.CharField (max_length=20)
	Celular=models.CharField (max_length=10)
	Email=models.CharField (max_length=50)
	Direccion=models.CharField (max_length=30)
    Cedula_pac=models.CharField (max_length=10)
	Cedula_pac=  models.ForeignKey(Cedula_pac.related_model'Paciente',on_delete=models.cascade)

	
