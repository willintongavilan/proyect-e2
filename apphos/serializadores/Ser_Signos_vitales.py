from dataclasses import fields
from rest_framework import serializers
from apphos.models.signos_vitales import Signos_vitales

class pacenteserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Signos_vitales
        fields=('Id_signos,Fecha,Hora,Oximetria,Frec_respirato,Frec_cardiaca,Temperatura,Presion_arterial,Glisemia,Cedula_paciente')
