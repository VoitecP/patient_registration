from django_filters.rest_framework import FilterSet
from patientes.models import *

class PatientFilter(FilterSet):
    class Meta:
        model=Patient
        fields={
            'id':['exact'],
            'name':['exact'],
            'surname':['exact'],   
        }

class DoctorFilter(FilterSet):
    class Meta:
        model=Doctor
        fields={
            'id':['exact'],
            'name':['exact'],
            'surname':['exact'],  
        }


class VisitFilter(FilterSet):
    class Meta:
        model=Visit
        fields={
            'id':['exact'],
            'patient':['exact'],  
            'doctor':['exact'],
            'price': ['gt','lt'],
            
        }

class CategoryFilter(FilterSet):
    class Meta:
        model=Category
        fields={
            'id':['exact'],
            'name':['exact'],  

        }