from django.db import models

class Historia_clinica(models.model):
    
    id_historia=models.CharField (primary_key=true)
	diagnostico=models.CharField (max_length=1000)
	sugerencia=models.CharField (max_length=1000)
	cedula_paciente=  models.ForeignKey(Cedula_paciente.related_model'Paciente',on_delete=models.cascade)
	login =models.ForeignKey (login.related_model'login',on_delete=models.cascade)
