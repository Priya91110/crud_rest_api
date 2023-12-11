from rest_framework.parsers import JSONParser 
from django.shortcuts import render
from django.http  import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# user decorator which ignore csrf
@csrf_exempt
def employeeListView(request):
    if request.method == "GET":
        emplolyees = Employee.objects.all()
        # converting python query object into json using serializer
        serializer = EmployeeSerializer(emplolyees, many = True)
        # serializer.data means data converted into json
        # json is string so we have to write safe=False
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        # to parse json
        jsondata = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
        
def UserListView(request):
    users_data = User.objects.all()
    serializer = UserSerializer(users_data, many=True)
    return JsonResponse(serializer.data, safe=False)

# primary key based operation for delete, update

@csrf_exempt
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)
    
    # to delete api/employee/4
    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    #get via id api/employee/5
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        jsondata = JSONParser.parse(request)
        serializer = EmployeeSerializer(employee, data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
