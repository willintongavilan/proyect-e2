from django.db import models

from apphos.models.Auxiliar import Auxiliar
from apphos.models.Login import login
from apphos.models.Historia_clinica import Historia_clinica
from apphos.models.Medico import Medico
from apphos.models.Auxiliar import Auxiliar
from apphos.models.Paciente import Paciente

class Enfermero(models.model):
    cedula_enfe=models.CharField (primary_key=True)
    nombre=models.CharField (max_length=20)
    apellido_1=models.CharField (max_length=20)
    apellido_2=models.CharField (max_length=20)
    numtel_enfe=models.CharField (max_length=10)
    Historia_clinica=models.ForeignKey (Historia_clinica, related_name='Historia_clinica',on_delete=models.CASCADE)
    login =models.ForeignKey (login, related_name='login',on_delete=models.CASCADE)
    cedula_med=  models.ForeignKey (Medico, related_name='paciente',on_delete=models.CASCADE)
    Auxiliar = models.ForeignKey (Auxiliar, related_name='Auxiliar', on_delete=models.CASCADE)
    Paciente = models.ForeignKey (Paciente, related_name='Paciente', on_delete=models.CASCADE)
    
