from rest_framework.parsers import JSONParser 
from django.shortcuts import render
from django.http  import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# use csrf_exempt decorator which ignore csrf
# this function for show data(GET) and add data(POST)
# @csrf_exempt
@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == "GET":
        emplolyees = Employee.objects.all()
        # converting python query object into json using serializer
        serializer = EmployeeSerializer(emplolyees, many = True)
        # serializer.data means data converted into json
        # json is string so we have to write safe=False
        # return JsonResponse(serializer.data, safe=False)
        # if we are using api_view we have to use Response
        return Response(serializer.data)
    
    
    elif request.method == "POST":
        # to parse json
        # jsondata = JSONParser().parse(request)
        # here we don't need parser if we are using request
        # serializer = EmployeeSerializer(data=jsondata)
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
  
# primary key based operation for delete, update

# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=404)
    
    # to delete api/employee/4
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #get via id api/employee/5
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# To show all the users including admin   

def UserListView(request):
    users_data = User.objects.all()
    serializer = UserSerializer(users_data, many=True)
    return JsonResponse(serializer.data)
