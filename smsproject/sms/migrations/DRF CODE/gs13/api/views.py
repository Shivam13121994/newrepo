# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin # ListModelMixin for get and CreateModelMixin for post

class StudentList(GenericAPIView, ListModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs ):
        return self.list(request, *args, **kwargs)
    
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self, request, *args, **kwargs ):
        return self.create(request, *args, **kwargs)
    
class StudentRetrieve(GenericAPIView, RetrieveModelMixin):  # This is for particular data retrieval 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs ):
        return self.retrieve(request, *args, **kwargs)
    
class StudentUpdate(GenericAPIView, UpdateModelMixin):  # it will work for put and patch
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs ):
        return self.update(request, *args, **kwargs)
    
class StudentDestroy(GenericAPIView, DestroyModelMixin):  # it will work for put and patch
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def delete(self, request, *args, **kwargs ):
        return self.destroy(request, *args, **kwargs)
    
    
    

