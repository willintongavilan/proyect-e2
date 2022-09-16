from django.db import models

class paciente(models.model):
    
    Id_signos=models.CharField (primary_key=true)
	Fecha=models.CharField (max_length=10)
	Hora=models.CharField (max_length=10)
	Oximetria=models.CharField (max_length=10)
	Frec_respirato=models.CharField (max_length=10)
	Frec_cardiaca=models.CharField (max_length=20)
	Temperatura=models.CharField (max_length=10)
    Presion_arterial=models.CharField (max_length=10)
    Glisemia=models.CharField (max_length=10)
	Cedula_paciente=  models.ForeignKey(Cedula_paciente.related_model'paciente',on_delete=models.cascade)

