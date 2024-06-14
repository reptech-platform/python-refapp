#from django.contrib import urls
from django.urls import path, include
from . import views

urlpatterns=[
path('persons/', views.personGetlist),
path('persons/<int:pk>/', views.personGetdetail),
path('persons/trips/', views.tripGetlist),
path('persons/<int:pk>/trips/', views.tripsGetFulldetails),
path('persons/<int:pk>/trips/<int:tk>/', views.tripsGetPerdetails),
path('persons/<int:pk>/attachments/', views.personGetattachment),
path('persons/<int:pk>/attachments/<int:tk>/', views.personGetPerattachment),
path('person/', views.personPostlist),
path('person/<int:pk>/', views.personPutdetail),
path('person/attachments/', views.PersonPostattachment),
path('person/trips/',views.tripPostlist),
path('person/<int:pk>/trips/<int:tk>/',views.tripPutdetail),
path('persons1/<int:pk>/',views.personDeldetail),
path('persons1/<int:pk>/attachments/<int:tk>/',views.personDelattachment),
path('persons1/<int:pk>/trips/',views.tripDelAlldetails),
path('persons1/<int:pk>/trips/<int:tk>/',views.tripDelPerdetails),

]
