from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name']
    filterset_fields = ['name','city']
    

    
    # Above function is used for show the passby students from a particular user
    # means when user1 is login only those students who are passed by user1 will be shown 
    # shown in the system.
    