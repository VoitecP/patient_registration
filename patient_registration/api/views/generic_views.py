from patientes.models import *
from ..serializers import *
from api.filters import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class PatientsGeneric(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes=[IsAuthenticated]

    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class=PatientFilter
    search_fields=['name','surname','citizen_id']
    ordering_fields=['citizen_id', 'name', 'surname'] 

    # def get_queryset(self):
    #     return super().get_queryset()


class PatientGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



class DoctorsGeneric(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class=DoctorFilter
    search_fields=['id','name','surname']
    ordering_fields=['specialisation', 'name', 'surname'] 


class DoctorGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[IsAuthenticated]



class CategoriesGeneric(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=CategoryFilter        
    search_fields=['id','name']
    ordering_fields=['id', 'name'] 
    


class CategoryGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes=[IsAuthenticated]



class VisitsGeneric(ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=VisitFilter        
    search_fields=['id','patient__name','patient__surname']
    ordering_fields=['description', 'patient__name', 'patient__surname','category'] 


class VisitGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes=[IsAuthenticated]