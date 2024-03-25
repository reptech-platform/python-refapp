from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person

# Create your views here.
def member(request):
    member=Person.objects.all().values()
    template=loader.get_template('Allperson.html')
    context={
        'member':member
    }
    
    return HttpResponse(template.render(context,request))

def details(request,id):
    member1=Person.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'member1':member1
    }
    return HttpResponse(template.render(context,request))