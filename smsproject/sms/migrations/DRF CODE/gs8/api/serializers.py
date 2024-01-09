from rest_framework import serializers
from .models import Student

# def start_with_r(value):
#     if value[0].lower()!= 'r':
#         raise serializers.ValidationError('Name should be start with R')

class StudentSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower()!= 'r':
            raise serializers.ValidationError('Name should be start with R')
        
    name = serializers.CharField(validators = [start_with_r] )
    class Meta:
       model = Student
       fields = ['name', 'roll', 'city']
   
   
   
   
   
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats Full')
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'veeru' and ct.lower()!= 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data

        
    
    
  
        

