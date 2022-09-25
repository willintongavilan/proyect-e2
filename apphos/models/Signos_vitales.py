from socket import PACKET_BROADCAST
from django.db import models
from apphos.models.Paciente import Paciente
from apphos.models.Familiar import Familiar
from apphos.models.Medico import Medico
from apphos.models.Historia_clinica import Historia_clinica

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
 cedula_pac=models.ForeignKey(Paciente,related_name='paciente',on_delete=models.CASCADE)
 Medico=models.ForeignKey(Medico,related_name='medico',on_delete=models.CASCADE)
 Historia_clinica=models.ForeignKey(Historia_clinica,related_name='historia_clinica',on_delete=models.CASCADE)
 Familiar=models.ForeignKey(Familiar,related_name='familiar',on_delete=models.CASCADE)
 Paciente=models.ForeignKey(Paciente,related_name='Paciente',on_delete=models.CASCADE)
 
