from django.db import models
from apphos.models.Paciente import Paciente
from apphos.models.Familiar import Familiar

from apphos.models.Historia_clinica import Historia_clinica

class Signos_vitales(models.Model):
    
 Id_signos=models.CharField (primary_key=True, max_length=40)
 fecha=models.CharField (max_length=25)
 Hora=models.CharField (max_length=25)
 Oximetria=models.CharField (max_length=25)
 Frec_respirato=models.CharField (max_length=25)
 Frec_cardiaca=models.CharField (max_length=25)
 Temperatura=models.CharField (max_length=25)
 presion_arterial=models.CharField (max_length=25)
 Glisemia=models.CharField (max_length=25)
 cedula_pac=models.ForeignKey(Paciente,related_name='Signos_vitales',on_delete=models.CASCADE)

 Historia_clinica=models.ForeignKey(Historia_clinica,related_name='Signos_vitales',on_delete=models.CASCADE)
 Familiar=models.ForeignKey(Familiar,related_name='Signos_vitales',on_delete=models.CASCADE)
 
