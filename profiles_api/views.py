from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """ TEST Api View """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """ Return List of api fetaure """
        an_apiview = [
            'APIView seems traditional view of django',
            'You write logic in APIView',
            'it mapped manually to URL'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """ Create hello message with our name """
        print('Data :',request.data)
        serializer = self.serializer_class(data=request.POST)

        if serializer.is_valid():
            print(serializer.validated_data)
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        """ Handle partial updating an object """
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'message':'DELETE'})
