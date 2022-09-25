from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apphos.serializadores.Ser_Historia_clinica import historiaclinicaserializer
from apphos.models.Historia_clinica import Historia_clinica

class detailhistoriaclinicaview(APIView): 
    def get(self, request, pk, format=None):
        snippet = Historia_clinica.objects.get(pk=pk)
        serializer = Historia_clinica(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = Historia_clinica.objects.get(pk=pk)
        serializer = Historia_clinica(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Historia_clinica.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)