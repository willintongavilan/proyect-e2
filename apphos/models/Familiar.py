from django.db import models

class Familiar(models.model):
    cedula_fam=models.CharField (primary_key=true)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    celular=models.CharField (max_length=10)
    email=models.CharField (max_length=50)
    direccion=models.CharField (max_length=30)
    cedula_pac=models.CharField (max_length=10)
    cedula_pac=  models.ForeignKey(Cedula_pac.related_model'paciente',on_delete=models.cascade)

	
