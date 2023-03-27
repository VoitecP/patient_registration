from patientes.models import *
from ..serializers import *
from api.filters import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PatientViewSet(ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class=PatientFilter        
    search_fields=['name','surname','citizen_id']
    ordering_fields=['citizen_id', 'name', 'surname'] 
   
    
class DoctorViewSet(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    permission_classes=[IsAuthenticated] 
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=DoctorFilter        
    search_fields=['id','name','surname']
    ordering_fields=['specialisation', 'name', 'surname'] 


class VisitViewSet(ModelViewSet):
    queryset=Visit.objects.all()
    serializer_class=VisitSerializer
    permission_classes=[IsAuthenticated] 
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=VisitFilter        
    search_fields=['id','patient__name','patient__surname']
    ordering_fields=['description', 'patient__name', 'patient__surname','category'] 


class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated] 
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=CategoryFilter        
    search_fields=['id','name']
    ordering_fields=['id', 'name'] 








#  Opinion model to implement and add to Nested Router
# class OpinionViewSet(ModelViewSet):
#     serializer_class=OpinionSerializer

#     def get_queryset(self):
#         queryset=Opinion.objects.filter(visit_id=self.kwargs["visit_pk"])
#         return queryset

#     def get_serializer_context(self):
#         context={"visit_id":self.kwargs["visit_pk"]}
#         return context