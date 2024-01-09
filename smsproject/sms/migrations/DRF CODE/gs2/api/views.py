from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata) # changed pythondata to complex data here
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}  # this is response messsage
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json' )
        json_data = JSONRenderer().render(serializer.errors) # this is else part
        return HttpResponse(json_data, content_type = 'application/json' )
            
            
# TO run this view we have to write urls 
        
        

