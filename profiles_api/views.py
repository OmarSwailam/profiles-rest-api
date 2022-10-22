from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, formate=None):
        dum_list = [
            "object1",
            "object2",
            "object3",
            "object4",
        ]
        return Response({
            "message": "Hello Api",
            "dum_list": dum_list
        })
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )