from dataclasses import fields
from rest_framework import serializers
from apphos.models.Familiar import Familiar

class familiarserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Familiar
        fields=('cedula_fam','nombre','apellido_1','apellido_2','celular','email','direccion',
                'cedula_pac','login','Auxilar','Paciente')
