from django.shortcuts import render

from django.http import HttpRequest,HttpResponse,JsonResponse
# Create your views here.
from rest_framework import viewsets
from .models import Company,Employee,PersonalDetails
from .serializers import CompanySerializer,EmployeeSerializer,PersonalSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    #company/{id}/employee
    @action(detail=True,methods=['get'])
    def employee(self,request,pk):
        try:
            company=Company.objects.get(pk=pk)
            employee=Employee.objects.filter(company=company)
            emp_serial=EmployeeSerializer(employee,many=True,context={'request':request})
            return Response(emp_serial.data)
        except:
            return Response({
                'message':"Company does not exist"
            })
    
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    @action(detail=True,methods=['get'])
    def personal_details(self,request,pk):
        employee=Employee.objects.get(pk=pk)
        details=PersonalDetails.objects.filter(employee=employee)
        detail_serial=PersonalSerializer(details,many=True,context={'request':request})
        return Response(detail_serial.data)
        
            

class PersonalViewset(viewsets.ModelViewSet):
    queryset=PersonalDetails.objects.all()
    serializer_class=PersonalSerializer
    

def index(request):
    return HttpResponse("New Api is working")
    