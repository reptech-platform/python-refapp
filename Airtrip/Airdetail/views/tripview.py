from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ..models import Person,Trip,Airline,Airport,Document,Address
from rest_framework import serializers
from ..serializer.tripserializer import TripSerializer
from rest_framework.decorators import api_view

# Create your views here.
 
@csrf_exempt
@api_view(['GET'])
def tripGetlist(request):
        trips=Trip.objects.all()
        serializer=TripSerializer(trips,many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
    
@csrf_exempt
@api_view(['POST'])
def tripPostlist(request):
        print("post method call")
        data=JSONParser().parse(request)
        serializer=TripSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
@api_view(['GET'])
def tripsGetFulldetails(request,pk):
    try:
        person=Person.objects.get(pk=pk)
    except Person.DoesNotExist: 
        return JsonResponse ({'error': 'Trip does not exist'}, status=404)
         
    trips=Trip.objects.filter(personId=person)
    serializer=TripSerializer(trips,many=True)
    return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
@api_view(['GET'])
def tripsGetPerdetails(request,pk,tk):
    try:
        person=Person.objects.get(id=pk)
        trips=Trip.objects.get(id=tk,personId=person)
    except (Person.DoesNotExist, Trip.DoesNotExist):
        return JsonResponse({'error': 'Trip does not exist'}, status=404)
    serializer=TripSerializer(trips)
    return JsonResponse(serializer.data, status=200)
         

@csrf_exempt
@api_view(['PUT'])
def tripPutdetail(request,pk,tk):

    try:
        persons=Person.objects.get(id=pk)
        trips=Trip.objects.get(id=tk,personId=persons)
    except (Person.DoesNotExist,Trip.DoesNotExist):
        return JsonResponse ({'error': 'Person/Trip does not exist'},status=404)
    data=JSONParser().parse(request)
    serializer=TripSerializer(instance=trips,data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors , status=400)

@csrf_exempt
@api_view(['DELETE'])
def tripDelAlldetails(request,pk):
    try:
        person=Person.objects.get(pk=pk)
    except Person.DoesNotExist: 
        return JsonResponse ({},status=404)
         
    trips=Trip.objects.filter(personId=person)
    trips.delete()
    return JsonResponse({},status=204)     

@csrf_exempt
@api_view(['DELETE'])
def tripDelPerdetails(request,pk,tk):

    try:
        person=Person.objects.get(id=pk)
        trips=Trip.objects.get(id=tk)
    except (Person.DoesNotExist,Trip.DoesNotExist): 
        return JsonResponse ({},status=404)     

    trips.delete()
    return JsonResponse({},status=204)
    


