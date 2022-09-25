from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apphos.serializadores.Ser_paciente import pacienteserializer
from apphos.models.Paciente import Paciente

class detailpacienteview(APIView): 
    def get(self, request, pk, format=None):
        snippet = Paciente.objects.get(pk=pk)
        serializer = Paciente(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = Paciente.objects.get(pk=pk)
        serializer = Paciente(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Paciente.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)