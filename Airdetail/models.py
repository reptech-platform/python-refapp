from enum import Enum
from django.db import models
#from djongo import models
#from djongo.models.fields import ArrayModelField
from django.contrib.postgres.fields import ArrayField
from django.db import models 


#Address Model or table is created seperately to hold the addressinfo and homeaddress info of a any person created and which is related to person fields.
class Address(models.Model):
             name=models.CharField(max_length=100, default=True)
             country=models.CharField(max_length=100, default=True)
             region=models.CharField(max_length=100, default=True)
             address=models.CharField(max_length=100, default=True)
             city=models.CharField(max_length=100, default=True)
             buildinginfo=models.CharField(max_length=100, default=True)
             

#Person table will capture all the required fields of person including addressinfo and homeaddress info which will store in diff table.             
class Person(models.Model):
        
        GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
        FEATURE_CHOICES = [
        ('feature1', 'Feature 1'),
        ('feature2', 'Feature 2'),
        ('feature3', 'Feature 3'),
        ('feature4', 'Feature 4'),
    ]
        

        userName=models.CharField(max_length=100, default=' ')
        firstName=models.CharField(max_length=100)
        lastName=models.CharField(max_length=100)
        income=models.DecimalField(max_digits=100,decimal_places=3)
        dateOfBirth=models.DateField()
        photo=models.ImageField()
        middleName=models.CharField(max_length=100, default=' ')
        gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
        age=models.SmallIntegerField()
        emails = ArrayField(models.EmailField(), blank=True,default=list)       
        favoriteFeature=models.TextField()
        features=models.CharField(max_length=200, choices=FEATURE_CHOICES)
        
        addressInfo = models.ForeignKey(Address,related_name='addressInfo' ,on_delete=models.CASCADE, default=None)
        homeAddress=models.ForeignKey(Address,related_name='homeAddress', on_delete=models.CASCADE, default=None)
#Document table which holds document type and file along with the person ID.
class Document(models.Model):
       personId=models.ForeignKey(Person, on_delete=models.CASCADE)
       document_type=models.CharField(max_length=100)
       file=models.FileField(upload_to='documents/')

class Trip(models.Model):
        tripId=models.SmallIntegerField()
        shareId=models.TextField()
        name=models.CharField(max_length=100)
        budget=models.BigIntegerField()
        description=models.TextField()
        startsAt=models.DateField()
        endsAt=models.DateField()
        startTime=models.TimeField(null=True)
        endTime=models.TimeField(null=True)
        cost=models.FloatField()
        personId=models.ForeignKey(Person, on_delete=models.CASCADE)
        

class Airline(models.Model):    
        airlineCode=models.CharField(max_length=100)
        name=models.CharField(max_length=100)
        logo=models.ImageField()
    
class Airport(models.Model):
        name=models.CharField(max_length=100)
        icaoCode=models.CharField(max_length=50)
        iataCode=models.CharField(max_length=100)
        location=models.JSONField(blank=True,null=True)
        latitude=models.FloatField()
        longitude=models.FloatField()
        isInsideCity=models.BooleanField()
        location=models.JSONField(blank=True,null=True)
