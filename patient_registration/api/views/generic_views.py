from api.filters import *
from ..serializers import *
from patientes.models import *

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PatientsGeneric(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # def get_queryset(self):
    #     return super().get_queryset()


class PatientGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer



class DoctorsGeneric(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer



class CategoriesGeneric(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class VisitsGeneric(ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer