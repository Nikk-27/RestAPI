from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer

class employeeList(APIView):

    def get(self, request):              ## to return al the employees in the model, getting or reading all your data
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many = True)     ## convert those employees to json
        return Response(serializer.data)

    def post(self):             ## to create new employee, submitting all your data
        pass


