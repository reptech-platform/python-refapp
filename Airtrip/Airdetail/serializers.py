from django.contrib.auth.models import User
from .models import Person,Trip, Airline, Airport, Document,Address
 
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=['name','country','region','address','city','buildinginfo']	

class PersonSerializer(serializers.ModelSerializer):
    addressInfo=AddressSerializer(required=False)
    homeAddress=AddressSerializer(required=False)
    address_id = serializers.PrimaryKeyRelatedField(source='addressInfo', read_only=True)
    homeAddress_id = serializers.PrimaryKeyRelatedField(source='homeAddress', read_only=True)
	
    class Meta:
        model=Person
        fields=['userName', 'firstName', 'lastName', 'income', 'dateOfBirth', 'middleName', 'gender', 'age','addressInfo','homeAddress','address_id','homeAddress_id']
       
     	
    def to_representation(self, instance):
    	rep = super().to_representation(instance)
    	rep['address_id'] = instance.addressInfo_id
    	rep['homeAddress_id'] = instance.homeAddress_id
    	return rep
    	 	
    def create(self, validated_data):
        address_info_data = validated_data.pop('addressInfo', None)
        home_address_data = validated_data.pop('homeAddress', None)
        
        person_instance = Person(**validated_data)
        if address_info_data:
            address_info_instance = Address.objects.create(**address_info_data)
            person_instance.addressInfo = address_info_instance
            
        if home_address_data:
            home_address_instance = Address.objects.create(**home_address_data)
            person_instance.homeAddress = home_address_instance
            
        person_instance.save() 
        return person_instance
    
    def update(self, instance, validated_data):
        address_info_data = validated_data.pop('addressInfo', None)
        home_address_data = validated_data.pop('homeAddress', None)

        # Update fields directly belonging to the Person model
        instance.userName = validated_data.get('userName', instance.userName)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.income = validated_data.get('income', instance.income)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.middleName = validated_data.get('middleName', instance.middleName)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)

        # Update addressInfo if provided
        if address_info_data:
            address_info_instance, _ = Address.objects.get_or_create(**address_info_data)
            instance.addressInfo = address_info_instance

        # Update homeAddress if provided
        if home_address_data:
            home_address_instance, _ = Address.objects.get_or_create(**home_address_data)
            instance.homeAddress = home_address_instance

        # Save the changes to the instance
        instance.save()
        return instance
        

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=['personId', 'document_type', 'file']
        #fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trip
        
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airline
        fields=['airlineCode', 'name', 'logo']

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Airport
        fields=['name', 'icaoCode', 'iataCode', 'location', 'latitude', 'longitude', 'isInsideCity']
