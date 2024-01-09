from rest_framework import serializers
from .models import SMSModel 

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSModel
        fields = ['id','Mobile_no']
