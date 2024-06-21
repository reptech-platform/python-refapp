from django.contrib.auth.models import User
from ..models import Document
 
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=['personId', 'document_type', 'file']
        #fields = '__all__'


