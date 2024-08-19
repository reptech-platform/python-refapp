from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ..models import Person,Trip,Airline,Airport,Document,Address
from rest_framework import serializers
from ..serializer.tripserializer import TripSerializer
from rest_framework.decorators import api_view,permission_classes
from django.db.models import Q 
from rest_framework.permissions import AllowAny

# Create your views here.
 
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def tripGetlist(request):
        trips=Trip.objects.all().order_by('budget')[:50]
        serializer=TripSerializer(trips,many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
    
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def tripsGetFulldetails(request,pk):
    try:
        person=Person.objects.get(pk=pk)
    except Person.DoesNotExist: 
        return JsonResponse ({'error': 'Trip does not exist'}, status=404)
         
    trips=Trip.objects.filter(personId=person)[:50]
    serializer=TripSerializer(trips,many=True)
    return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def tripDelPerdetails(request,pk,tk):

    try:
        person=Person.objects.get(id=pk)
        trips=Trip.objects.get(id=tk)
    except (Person.DoesNotExist,Trip.DoesNotExist): 
        return JsonResponse ({},status=404)     

    trips.delete()
    return JsonResponse({},status=204)
    
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def tripSearchGetlist(request):
        
        search_query=request.GET.get('search')
        trips=Trip.objects.all().filter(startsAt=search_query)
        serializer=TripSerializer(trips,many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
        
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def tripSearchGetlist(request,pk):
        
    try:   
        person=Person.objects.get(id=pk)
        #trips=Trip.objects.get(id=tk)
    except (Person.DoesNotExist,Trip.DoesNotExist):
    	return JsonResponse ({},status=404)
    	 
    	    
    search_query=request.GET.get('search')
    trips=Trip.objects.all().filter(Q(startsAt=search_query) & Q(personId=person))
    serializer=TripSerializer(trips,many=True)
    return JsonResponse(serializer.data, safe=False,status=200)

