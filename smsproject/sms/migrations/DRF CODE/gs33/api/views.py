from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user  # In self.request.user there is always current user
        return Student.objects.filter(passby = user)
    
    # Above function is used for show the passby students from a particular user
    # means when user1 is login only those students who are passed by user1 will be shown 
    # shown in the system.
    