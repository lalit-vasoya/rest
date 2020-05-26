from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import  api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
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


class HelloViewSet(viewsets.ViewSet):
    """ Test Api ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        an_viewset = [
            'Use actions (list,create,retrieve,update,pratial_update)',
            'Automatically maps to the Url router',
            'provide many functionality with less code'
        ]

        return Response({'message':'Hello!','an_viewset':an_viewset})

    def create(self,request):
        """ Create hello message with name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting object by IDS """
        return Response({'message':'Retrieve'})

    def update(self,request,pk=None):
        """ Handling update an object """
        return Response({'message':'PUT'})

    def partial_update(self, request, pk=None):
        """ Handling partial update """
        return Response({'message':'PATCH'})

    def destroy(self,request,pk=None):
        """ Delete an object """
        return Response({'message':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Create and  Updating User Profile """
    # for required configration
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #for authentication and permission
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    #for filters
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')


class UserLoginApiView(ObtainAuthToken):
    """ Handle create user authentication token """
    # print(api_settings.DEFAULT_RENDERER_CLASSE)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handel Create Reading Update profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self,serializer):
        """ Set User profile to the login user """
        print('First----------------------')
        serializer.save(user_profile=self.request.user)
