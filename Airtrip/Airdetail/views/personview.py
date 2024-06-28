from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ..models import Person,Trip,Airline,Airport,Document,Address
from rest_framework import serializers
from ..serializer.personserializer import PersonSerializer, AddressSerializer
from ..serializer.documentserializer import DocumentSerializer
from rest_framework.decorators import api_view

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def personGetlist(request):
    
        persons=Person.objects.all()
        serializer=PersonSerializer(persons,many=True,context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt 
@api_view(['POST'])
def personPostlist(request):
	
    #if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)	
        
   

@csrf_exempt    
@api_view(['GET'])
def personGetdetail(request,pk):
    try:
        persons=Person.objects.get(pk=pk)
    
    except Person.DoesNotExist:
        return JsonResponse ({'error': 'Person not found'},status=404)

    serializer=PersonSerializer(persons)
    return JsonResponse (serializer.data)
    
@csrf_exempt
@api_view(['PUT'])
def personPutdetail(request,pk):
    try:
        persons=Person.objects.get(pk=pk)
    except (Person.DoesNotExist):
        return HttpResponse (status=404)
    data=JSONParser().parse(request)
    serializer=PersonSerializer(instance=persons,data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors , status=400)

@csrf_exempt
@api_view(['DELETE'])
def personDeldetail(request,pk):
    try:
        person=Person.objects.get(pk=pk)
        persondoc=Document.objects.filter(personId=person)
    
    except Person.DoesNotExist:
        return JsonResponse ({},status=404)
        
    person.delete()
    persondoc.delete()
    return JsonResponse({},status=204)
    
@csrf_exempt
@api_view(['GET'])
def personGetattachment(request,pk):
    try:
        person=Person.objects.get(pk=pk)
        persondoc=Document.objects.filter(personId=person)
    except (Person.DoesNotExist,Document.DoesNotExist):
        return JsonResponse ({'error': 'Attachment does not exist'},status=404)

    serializer=DocumentSerializer(persondoc,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
@api_view(['POST'])
def PersonPostattachment(request):
    data=request.data
    serializer=DocumentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.error,400)


@csrf_exempt
@api_view(['GET'])
def personGetPerattachment(request,pk,tk):
    try:
        person=Person.objects.get(id=pk)
        persondoc=Document.objects.get(id=tk,personId=person)
    except (Person.DoesNotExist, Document.DoesNotExist):
        return JsonResponse({'error': 'Document does not exist'}, status=404)
    serializer=DocumentSerializer(persondoc)
    return JsonResponse(serializer.data, status=200)


@csrf_exempt
@api_view(['DELETE'])
def personDelattachment(request,pk,tk):
    try:        
        person=Person.objects.get(id=pk)
        persondoc=Document.objects.filter(id=tk,personId=person)  
    except (Person.DoesNotExist,Document.DoesNotExist):
        return JsonResponse({},status=404)

    persondoc.delete()
    return JsonResponse({},status=204)
 

