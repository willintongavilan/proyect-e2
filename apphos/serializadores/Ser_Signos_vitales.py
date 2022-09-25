from dataclasses import fields
from rest_framework import serializers
from apphos.models.Signos_vitales import Signos_vitales

class signosvitalesserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Signos_vitales
        fields=('Id_signos','Fecha,Hora','Oximetria','Frec_respirato','Frec_cardiaca',
                'Temperatura','Presion_arterial','Glisemia','Cedula_paciente','Medico',
                'Historia_clinica','Familiar','Paciente')
