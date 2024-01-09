from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only = True)    # First vidhi
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']  # we can use __all__ as well as exclude for fields
        #read_only_fields = ['name','roll']             # Second Vidhi
        extra_kwargs = {'name' : {'read_only':True} }        

   
    



