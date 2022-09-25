from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apphos.serializadores.Ser_Historia_clinica import Historia_clinica
class createhistoriaclinicaview(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = Historia_clinica(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
