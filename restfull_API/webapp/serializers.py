from rest_framework import serializers
from . models import employees

class employeesSerializer(serializers.ModelSerializer): ## converts model to json format

    class Meta:
        model = employees
        #fields = ('firstname','lastname')
        fields = '__all__'  #you can do this as well