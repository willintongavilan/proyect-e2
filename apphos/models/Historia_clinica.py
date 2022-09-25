from django.db import models
from apphos.models.Familiar import Familiar
from apphos.models.Medico import Medico
from apphos.models.Enfermero import Enfermero 
from apphos.models.Paciente import Paciente
from apphos.models.Historia_clinica import Historia_clinica
from apphos.models.Signos_vitales import signos_vitales
from apphos.models.Login import login
from apphos.models.Auxiliar import Auxiliar

class Historia_clinica(models.model):
    
   id_historia=models.CharField (primary_key=True)
   diagnostico=models.CharField (max_length=1000)
   sugerencia=models.CharField (max_length=1000)
   cedula_paciente=models.CharField (max_length=10)
   cedula_paciente= models.ForeignKey (Paciente, related_name='paciente',on_delete=models.CASCADE)
   login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
   Auxiliar = models.ForeignKey (Auxiliar, related_name='Auxiliar', on_delete=models.CASCADE)
   Familiar = models.ForeignKey (Familiar, related_name='Familiar',on_delete=models.CASCADE)
   Medico = models.ForeignKey (Medico, related_name='Medico', on_delete=models.CASCADE)
   Signos_vitales = models.ForeignKey (signos_vitales, related_name='Signos_vitales', on_delete=models.CASCADE)
   
