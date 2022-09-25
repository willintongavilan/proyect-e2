from dataclasses import fields
from rest_framework import serializers
from apphos.models.Paciente import Paciente

class pacienteserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Paciente
        fields=('cedula_pac','nombre','apellido_1','apellido_2','fecha_nto','direccion_pac','ciudad',
                'numtel_pac','cedula_med','cedula_enfe','Historia_clinica','login','Auxiliar','Medico',
                'Enfermero','Familiar')
