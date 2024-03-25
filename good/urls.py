from django.urls import path
from . import views

urlpatterns=[
    path('member/', views.member, name='member' ),
    path('member/details/<int:id>', views.details, name='details'),
]