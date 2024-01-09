from django.shortcuts import render
from rest_framework.decorators import api_view       # added
from rest_framework.response import Response         # added

# @api_view()                          # default is @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg' : 'Hello World'})

# @api_view(['POST'])                          
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg' : 'This is POST Request'})
    
@api_view(['GET','POST'])                          
def hello_world(request):
    if request.method == "GET":
        print(request.data)
        return Response({'msg' : 'This is GET Request'})
    if request.method == "POST":
        print(request.data)
        return Response({'msg' : 'This is POST Request', 'data' : request.data})
    
    



# Create your views here.
