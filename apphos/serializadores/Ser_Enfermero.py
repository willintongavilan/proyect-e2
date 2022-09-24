from dataclasses import fields
from rest_framework import serializers
from apphos.models.enfermero import Enfermero

class pacenteserializer(serializers.ModelSerializer):
     
 class Meta:
        model=Enfermero
        fields=('cedula_enfe,nombre,apellido_1,apellido_2,numtel_enfe'),
