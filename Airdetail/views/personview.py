from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ..models import Person,Trip,Airline,Airport,Document,Address
from rest_framework import serializers
from ..serializer.personserializer import PersonSerializer, AddressSerializer
from ..serializer.documentserializer import DocumentSerializer
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from django.db.models import Q,Count 
from rest_framework.permissions import AllowAny

# Create your views here.

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def personGetlist(request):
    
        persons=Person.objects.all().order_by('dateOfBirth')[:50]
        serializer=PersonSerializer(persons,many=True,context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt 
@api_view(['POST'])
@permission_classes([AllowAny])
def personPostlist(request):
	
    #if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)	
        
   

@csrf_exempt    
@api_view(['GET'])
@permission_classes([AllowAny])
def personGetdetail(request,pk):
    try:
        persons=Person.objects.get(pk=pk)
    
    except Person.DoesNotExist:
        return JsonResponse ({'error': 'Person not found'},status=404)

    serializer=PersonSerializer(persons)
    return JsonResponse (serializer.data)
    
@csrf_exempt
@api_view(['PUT'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def PersonPostattachment(request):
    data=request.data
    serializer=DocumentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.error,400)


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
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
@permission_classes([AllowAny])
def personDelattachment(request,pk,tk):
    try:        
        person=Person.objects.get(id=pk)
        persondoc=Document.objects.filter(id=tk,personId=person)  
    except (Person.DoesNotExist,Document.DoesNotExist):
        return JsonResponse({},status=404)

    persondoc.delete()
    return JsonResponse({},status=204)
    
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def personnameSearchGetlist(request): 
        search_query=request.GET.get('search')   
        persons=Person.objects.filter(firstName=search_query)
        serializer=PersonSerializer(persons,many=True,context={'request': request})
        return JsonResponse(serializer.data, safe=False)
        
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def personaddressSearchGetlist(request):
        search_query=request.GET.get('search')    
        persons=Person.objects.filter(Q(addressInfo__city=search_query) | Q(homeAddress__city=search_query)).distinct()
        serializer=PersonSerializer(persons,many=True,context={'request': request})
        return JsonResponse(serializer.data, safe=False)
 
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def persongroupGetlist(request): 
           
        #persons=Person.objects.filter(firstName=search_query)
        #data=Person.objects.values('gender','firstName').annotate(total=Count('gender')).order_by('gender')
        data=Person.objects.values('gender','firstName').order_by('gender')
        gender_Count=Person.objects.values('gender').annotate(total=Count('gender')).order_by('gender')
        countdata=[]
        newdata=[]
        for item in gender_Count:
             countdata.append({'Gender':item['gender'],
                            'Count':item['total']})
               
        for item in data:
             newdata.append({'Gender':item['gender'],
                            'Firstname':item['firstName']})
                            #'Count':item['total']})

        context={
             'Gendercount':countdata,
             'Details':newdata,
        }
        
        return Response (context)
        
        #return JsonResponse(data, safe=False)

