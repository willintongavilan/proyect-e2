from dataclasses import fields
from rest_framework import serializers
from .models import Paciente

class pacenteserializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__'
