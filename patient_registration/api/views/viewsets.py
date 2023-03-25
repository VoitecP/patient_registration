from patientes.models import *
from ..serializers import *
from api.filters import *

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

class PatientViewSet(ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class=PatientFilter        
    search_fields=['name','surname','citizen_id']
    ordering_fields=['citizen_id', 'name', 'surname'] 
   
    
class DoctorViewSet(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer


class VisitViewSet(ModelViewSet):
    queryset=Visit.objects.all()
    serializer_class=VisitSerializer


class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer




# class VisitViewSet(CreateModelMixin, RetrieveModelMixin,  DestroyModelMixin, GenericViewSet):
#     queryset= Visit.objects.all()
#     serializer_class=VisitSerializer
    #  Config Router..
    #  URLs     router.register("visits", views.VisitViewSet)



#  Opinion model to implement and add to Nested Router
# class OpinionViewSet(ModelViewSet):
#     serializer_class=OpinionSerializer

#     def get_queryset(self):
#         queryset=Opinion.objects.filter(visit_id=self.kwargs["visit_pk"])
#         return queryset

#     def get_serializer_context(self):
#         context={"visit_id":self.kwargs["visit_pk"]}
#         return context