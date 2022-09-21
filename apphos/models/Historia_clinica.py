from django.db import models

class Historia_clinica(models.model):
    
    Id_historia=models.CharField (primary_key=true)
	Diagnostico=models.CharField (max_length=1000)
	Sugerencia=models.CharField (max_length=1000)
	Cedula_paciente=  models.ForeignKey(Cedula_paciente.related_model'Paciente',on_delete=models.cascade)
