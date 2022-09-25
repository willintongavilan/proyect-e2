from dataclasses import fields
from rest_framework import serializers
from apphos.models.Enfermero import Enfermero

class enfermeroserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Enfermero
        fields=('cedula_enfe','nombre','apellido_1','apellido_2','numtel_enfe',
                'Historia_clinica','login','cedula_med','Auxlilar','Paciente')