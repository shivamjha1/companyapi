from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.core import serializers

from .models import Employees


# Create your views here.
def homepage(request):
    return HttpResponse("Hello World")
def emp(request,slug):
    return HttpResponse(slug+" name")


def apiex(request):
    employees = Employees.objects.all()
    employee_list = serializers.serialize('json', employees)
    return JsonResponse(employee_list, safe=False)