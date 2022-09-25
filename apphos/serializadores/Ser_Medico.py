from dataclasses import fields
from rest_framework import serializers
from apphos.models.Medico import Medico

class medicoserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Medico
        fields=('cedula_med','nombre','apellido_1','apellido_2','numtel_med','Historia_clinica'
              'login','Auxiliar','Paciente','Enfermero')
