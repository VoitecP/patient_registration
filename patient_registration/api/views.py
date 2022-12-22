
from api.filters import *
from .serializers import *
from patientes.models import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

class PatientViewSet(ModelViewSet):
    pagination_class=PageNumberPagination
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields=['id','name','surname']    
    filterset_class=PatientFilter           #instead of filterset_fields
    search_fields=['name','surname','citizen_id']   # works with  partial name one field to search looks thru fields
    ordering_fields=['citizen_id', 'name', 'surname']   # 'name'
    
class DoctorViewSet(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

# class VisitViewSet(CreateModelMixin, RetrieveModelMixin,  DestroyModelMixin, GenericViewSet):
#     queryset= Visit.objects.all()
#     serializer_class=VisitSerializer
    #  Config Router..
    #  URLs     router.register("visits", views.VisitViewSet)


class VisitViewSet(ModelViewSet):
    queryset=Visit.objects.all()
    serializer_class=VisitSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

#  Opinion model to implement and add to Nested Router
# class OpinionViewSet(ModelViewSet):
#     serializer_class=OpinionSerializer

#     def get_queryset(self):
#         queryset=Opinion.objects.filter(visit_id=self.kwargs["visit_pk"])
#         return queryset

#     def get_serializer_context(self):
#         context={"visit_id":self.kwargs["visit_pk"]}
#         return context