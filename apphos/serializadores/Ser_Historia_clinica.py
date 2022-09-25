from dataclasses import fields
from rest_framework import serializers
from apphos.models.Historia_clinica import Historia_clinica

class historiaclinicaserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Historia_clinica
        fields=('id_historia','diagnostico','sugerencia',
                'cedula_paciente','Auxiliar','Familiar','Medico','Signos_vitales')


