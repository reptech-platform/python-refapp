from django.db import models

# Create your models here.

class Person(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    city=models.CharField(max_length=200)
    phone=models.IntegerField()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"