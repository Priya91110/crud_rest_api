from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=10)
    
    # to save data(Via post method)
    def create(self, validated_data):
        # named args = **validated_data
        # print("Create method called")
        return Employee.objects.create(**validated_data)    
    
    #  to update data(via PUT method)
    # instance = employee (instance is which we have to update data employee )
    def update(self, empolyee, validated_data):
        # if it is dict and we have to pass named argument we have to user **
        newEmployee = Employee(**validated_data)
        newEmployee.id = empolyee.id
        newEmployee.save()
        return newEmployee

    
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=225)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=225)
    
    
    
