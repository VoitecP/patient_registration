from patientes.models import *
from ..serializers import *
from api.filters import *

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework import status

class Paginator(PageNumberPagination):
    page_size=4
    page_size_query_param = 'page_size'
    max_page_size=10
    template = 'rest_framework/pagination/numbers.html'


class PatientsApi(APIView):
    def get(self, request):
        queryset = Patient.objects.all()
        paginator=Paginator()
        paginated_queryset=paginator.paginate_queryset(queryset, request)
        serializer = PatientSerializer(paginated_queryset, many = True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)


class PatientApi(APIView):
    def get(self, request, pk):
        object = get_object_or_404(Patient, id = pk)
        serializer = PatientSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object = get_object_or_404(Patient, id = pk)
        serializer = PatientSerializer(object, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object = get_object_or_404(Patient, id = pk)
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class DoctorsApi(APIView):
    def get(self, request):
        queryset = Doctor.objects.all()
        paginator=Paginator()
        paginated_queryset=paginator.paginate_queryset(queryset, request)
        serializer = DoctorSerializer(paginated_queryset, many = True)
        return paginator.get_paginated_response(serializer.data)


    def post(self, request):
        serializer = DoctorSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)


class DoctorApi(APIView):
    def get(self, request, pk):
        object = get_object_or_404(Doctor, id = pk)
        serializer = DoctorSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object = get_object_or_404(Doctor, id = pk)
        serializer = DoctorSerializer(object, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object = get_object_or_404(Doctor, id = pk)
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



class CategoriesApi(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        paginator=Paginator()
        paginated_queryset=paginator.paginate_queryset(queryset, request)
        serializer = CategorySerializer(paginated_queryset, many = True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)


class CategoryApi(APIView):
    def get(self, request, pk):
        object = get_object_or_404(Category, id = pk)
        serializer = CategorySerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object = get_object_or_404(Category, id = pk)
        serializer = CategorySerializer(object, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object = get_object_or_404(Category, id = pk)
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class VisitsApi(APIView):
    def get(self, request):
        queryset = Visit.objects.all()
        paginator=Paginator()
        paginated_queryset=paginator.paginate_queryset(queryset, request)
        serializer = VisitSerializer(paginated_queryset, many = True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = VisitSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)


class VisitApi(APIView):
    def get(self, request, pk):
        object = get_object_or_404(Visit, id = pk)
        serializer = VisitSerializer(object)
        return Response(serializer.data)
    
    def put(self, request, pk):
        object = get_object_or_404(Visit, id = pk)
        serializer = VisitSerializer(object, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        object = get_object_or_404(Visit, id = pk)
        object.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)