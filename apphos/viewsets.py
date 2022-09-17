from rest_framework import viewsets
from . import models
from . import serializers

class Pacienteviewsets(viewsets.ModelViewSet):
    queryset=models.Paciente.objets.all()
    serializer_class=serializers.pacenteserializer
