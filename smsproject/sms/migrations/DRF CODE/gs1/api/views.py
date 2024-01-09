from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer         # for converting Complex data to python data
from rest_framework.renderers import JSONRenderer  # for converting python data to json data
from django.http import HttpResponse, JsonResponse

# Create your views here.
# Model object - Single Student Data 
# function based view

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)    # in these two lines complex data is changed to python data, if tou change id then data will change
    # print(stu)
    serializer = StudentSerializer(stu)  # in first line we made model object and in second we changed it in python object
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # this line is changing python data to json data
    # print(json_data)
    # now this data is sent to the client as a response
    return HttpResponse(json_data, content_type = 'application/json')

# Query Set - All Student Data 
def student_list(request):
    stu = Student.objects.all()    # in these two lines complex data is changed to python data, if tou change id then data will change
    # print(stu)
    serializer = StudentSerializer(stu, many= True)  # in first line we made model object and in second we changed it in python object
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # this line is changing python data to json data
    # print(json_data)
    # now this data is sent to the client as a response
    return HttpResponse(json_data, content_type = 'application/json')
    # you can send response using json response
    #return JsonResponse(serializer.data, safe=False)  # because it is non-dict
    
    
    


