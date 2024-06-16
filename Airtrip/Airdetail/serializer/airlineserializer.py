from django.contrib.auth.models import User
from .models import  Airline
 
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airline
        fields=['airlineCode', 'name', 'logo']


