from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter 
from .routers import router



urlpatterns =[
    path('api2/', include((router.urls,'api'))),
    
    #   {% url 'api:patients' %}
    # path('', PatientCreateView.as_view(), name='patients'),                  # temp view
    
    
    path('patients/<str:pk>/',PatientApi.as_view(),name='patient-api'),
    path('visits/', VisitsApi.as_view(),name='visits-api'),
    path('visits/<str:pk>/', VisitApi.as_view(),name='visit-api'),
    path('doctors/', DoctorsApi.as_view(),name='doctors-api'),
    path('doctors/<str:pk>/', DoctorApi.as_view(),name='doctor-api'),
    path('categories/', CategoriesApi.as_view(),name='categories-api'),
    path('categories/<str:pk>/', CategoryApi.as_view(),name='category-api'),
]


  
# from rest_framework.nested import routers        # Not installed yet  pip install drf-nested-routers


#             #    for   example nested path.. : patient/patient_<pk>/info/1  patient/1/info/1    
# patient_router = routers.NestedDefaultRouter(router,'patients', lookup='patient_pk')
