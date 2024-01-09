from django.shortcuts import render
from .models import SMSModel
from .serializers import SMSSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
import shortuuid
import xml.etree.ElementTree as ET
from .models import SMSModel
from django.core.serializers import serialize
from django.http import HttpResponse
import requests



class SMSModelViewSet(viewsets.ModelViewSet):
    queryset = SMSModel.objects.all()
    serializer_class = SMSSerializer
    authentication_classes = [JWTAuthentication]   # for basic Authentication with username password
  
    permission_classes = [IsAuthenticated]  # unauthenticated users have read permissions
    
    def create(self, request):
        serializer = SMSSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            s = shortuuid.ShortUUID(alphabet="0123456789")
            otp = s.random(length=5)
            Mobile_Number = request.data.get('Mobile_no')
            xml_code = '''

            <message-submit-request>
            <username>tridentindia</username>
            <password>tridentindia@1</password>
            <sender-id>TGROUP</sender-id>
            <MType>UNI</MType>
            <message-text>
            <text>Test</text>
            <to>9878998937</to>
            </message-text>
            </message-submit-request>'''







            url = "http://www.smsjust.com/sms/user/XMLAPI/send.php"

            payload = "<?xml version=\"1.0\"?>\r\n<message-submit-request>\r\n<username>tridentindia</username>\r\n<password>tridentindia@1</password>\r\n<sender-id>TGROUP</sender-id>\r\n<MType>UNI</MType>\r\n<message-text>\r\n<text>Test</text>\r\n<to>9878998937</to>\r\n</message-text>\r\n</message-submit-request>"
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            return Response({'msg' :'Data Created Successfully','Mobile_No':Mobile_Number,'OTP':otp}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    

    
    # def create(self, request, *args, **kwargs):
    #     s = shortuuid.ShortUUID(alphabet="0123456789")
    #     otp = s.random(length=5)
    #     #Mobile_NO = SMSModel()
    #     return Response({'success': 'Data successfully submitted','Otp':otp}, status=status.HTTP_200_OK)


    

    



