from django.db import models
from apphos.models.Familiar import Familiar
from apphos.models.Medico import Medico

from apphos.models.Paciente import Paciente


class Historia_clinica(models.Model):
    
   id_historia=models.CharField (primary_key=True)
   diagnostico=models.CharField (max_length=1000)
   sugerencia=models.CharField (max_length=1000)
   cedula_paciente=models.CharField (max_length=10)
   cedula_paciente= models.ForeignKey (Paciente, related_name='paciente',on_delete=models.CASCADE)
   
   Familiar = models.ForeignKey (Familiar, related_name='Familiar',on_delete=models.CASCADE)
   Medico = models.ForeignKey (Medico, related_name='Medico', on_delete=models.CASCADE)
 
   
