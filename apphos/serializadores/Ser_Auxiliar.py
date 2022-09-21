from dataclasses import fields
from rest_framework import serializers
from apphos.models.Auxiliar import Auxiliar

class pacenteserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Auxiliar
        fields=('cedula_aux,nombre,apellido_1,apellido_2,numtel_aux,'),
