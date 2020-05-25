from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Searialize name fields for our APIView """

    name = serializers.CharField(max_length=10)
    
