from django.contrib.auth.models import User
from ..models import Trip
 
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip
        
        fields = '__all__'


