#from django.contrib import urls
from django.urls import path, include
from .views import personview ,tripview

urlpatterns=[
path('persons/', personview.personGetlist),
path('persons/<int:pk>/', personview.personGetdetail),
path('persons/trips/', tripview.tripGetlist),
path('persons/<int:pk>/trips/', tripview.tripsGetFulldetails),
path('persons/<int:pk>/trips/<int:tk>/', tripview.tripsGetPerdetails),
path('persons/<int:pk>/attachments/', personview.personGetattachment),
path('persons/<int:pk>/attachments/<int:tk>/', personview.personGetPerattachment),
path('person/', personview.personPostlist),
path('person/<int:pk>/', personview.personPutdetail),
path('person/attachments/', personview.PersonPostattachment),
path('person/trips/', tripview.tripPostlist),
path('person/<int:pk>/trips/<int:tk>/', tripview.tripPutdetail),
path('persons1/<int:pk>/', personview.personDeldetail),
path('persons1/<int:pk>/attachments/<int:tk>/', personview.personDelattachment),
path('persons1/<int:pk>/trips/', tripview.tripDelAlldetails),
path('persons1/<int:pk>/trips/<int:tk>/', tripview.tripDelPerdetails),

]
