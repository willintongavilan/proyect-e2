from django.db import models

class paciente(models.model):
    
    Cedula_pac=models.CharField (primary_key=true)
	Nombre=models.CharField (max_length=20)
	Apellido_1=models.CharField (max_length=20)
	Apellido_2=models.CharField (max_length=20)
	Fecha_nto=models.CharField (max_length=20)
	Direccion_pac=models.CharField (max_length=20)
	Cedula_med=models.CharField (max_length=20)
	Cedula_enfe=models.CharField (max_length=20)
	Cedula_med = models.ForeignKey(Cedula_med.related_model)
	FOREIGN KEY (Cedula_enfe) REFERENCES Enfermero(Cedula_enfe))