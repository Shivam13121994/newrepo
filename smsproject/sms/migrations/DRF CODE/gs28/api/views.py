from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly         # for permissions

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]   # for basic Authentication with username password
    #permission_classes = [IsAuthenticated]           # for permission to login in api
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    
    
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

    
    
    
