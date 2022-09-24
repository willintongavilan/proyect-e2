from tokenize import Name
from django.db import models

class paciente(models.model):
    
 Id_signos=models.CharField (primary_key=True)
 fecha=models.CharField (max_length=10)
 Hora=models.CharField (max_length=10)
 Oximetria=models.CharField (max_length=10)
 Frec_respirato=models.CharField (max_length=10)
 Frec_cardiaca=models.CharField (max_length=20)
 Temperatura=models.CharField (max_length=10)
 presion_arterial=models.CharField (max_length=10)
 Glisemia=models.CharField (max_length=10)
 cedula_paciente=  models.ForeignKey(paciente,related_name='paciente',on_delete=models.cascade

