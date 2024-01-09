from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication  # for basic authentication
from rest_framework.permissions import IsAuthenticated
from .custompermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]   # for basic Authentication with username password
    permission_classes = [MyPermission]           # for permission to login in api
    
# if you want basic as well session authentication you can write it by giving comma
    
# If there are multiple classes and you want to give same basic authentication and permission 
# Then you can put these two lines globally and it will apply for all classes or you can apply all classes
# separately 
# for globally you go to setting.py and write any where 
# REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES' : ['rest_framework.authentication.BasicAuthetication'],
#    'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated']
#    }
#
#  Suppose there are multiple class and we want a particular class to permission all 
#  and others to isauthenticated then we can add these two lines in that class
#  authentication_classes = [BasicAuthentication] 
#  permission_classes = [AllowAny]
# Now all other classes will follow the global one but this particular api will follow local one
#
#
#

    
    
    
