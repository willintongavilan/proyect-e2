from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apphos.serializadores.Ser_Signos_vitales import signosvitalesserializer
from apphos.models.Signos_vitales import Signos_vitales

class detailsignosvitalessview(APIView): 
    def get(self, request, pk, format=None):
        snippet = Signos_vitales.objects.get(pk=pk)
        serializer = Signos_vitales(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = Signos_vitales.objects.get(pk=pk)
        serializer = Signos_vitales(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Signos_vitales.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)