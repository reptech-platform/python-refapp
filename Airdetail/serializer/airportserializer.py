from django.contrib.auth.models import User
from .models import  Airport
 
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields=['name', 'icaoCode', 'iataCode', 'location', 'latitude', 'longitude', 'isInsideCity']
