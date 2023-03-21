
from api.filters import *
from .serializers import *
from patientes.models import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from django.views.generic.edit import CreateView, UpdateView, DeleteView

#########

from rest_framework.views import APIView
from rest_framework.response import  Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

class PatientCreateView(CreateView):   # test view
    model=Patient
    fields='__all__'
    # success_url=reverse_lazy('patientes:patient-list')
    template_name='patient\patient_form.html'



class PatientsApi(APIView):
    def get(self, request):
        queryset=Patient.objects.all()
        serializer=PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PatientApi(APIView):
    def get(self, request, pk):
        object=get_object_or_404(Patient, id=pk)
        serializer=PatientSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object=get_object_or_404(Patient, id=pk)
        serializer=PatientSerializer(object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object=get_object_or_404(Patient, id=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DoctorsApi(APIView):
    def get(self, request):
        queryset=Doctor.objects.all()
        serializer=DoctorSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DoctorApi(APIView):
    def get(self, request, pk):
        object=get_object_or_404(Doctor, id=pk)
        serializer=DoctorSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object=get_object_or_404(Doctor, id=pk)
        serializer=DoctorSerializer(object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object=get_object_or_404(Doctor, id=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoriesApi(APIView):
    def get(self, request):
        queryset=Category.objects.all()
        serializer=CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CategoryApi(APIView):
    def get(self, request, pk):
        object=get_object_or_404(Category, id=pk)
        serializer=CategorySerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object=get_object_or_404(Category, id=pk)
        serializer=CategorySerializer(object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object=get_object_or_404(Category, id=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VisitsApi(APIView):
    def get(self, request):
        queryset=Visit.objects.all()
        serializer=VisitSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VisitApi(APIView):
    def get(self, request, pk):
        object=get_object_or_404(Visit, id=pk)
        serializer=VisitSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object=get_object_or_404(Visit, id=pk)
        serializer=VisitSerializer(object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object=get_object_or_404(Visit, id=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)