""" Usuario View"""

from rest_framework.views import APIView

from rest_framework import status

from rest_framework.response import Response

# Serailizer

from ..serializers.usuarios import *


class UsuarioLoginAPIView(APIView):
    """usuario login"""

    def post(self, request, *args, **kwargs):

        serializer = UsuarioLoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        usuario, token = serializer.save()

        data = {
            'user': UsuariorModelSerializer(usuario).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


class UsuarioSignupAPIView(APIView):
    """usuario login"""

    def post(self, request, *args, **kwargs):

        serializer = UsuarioSignupSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        usuario = serializer.save()

        data = UsuariorModelSerializer(usuario).data,
            
        return Response(data, status=status.HTTP_201_CREATED)
