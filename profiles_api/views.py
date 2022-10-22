from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

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