from django.urls import path
from ..views.doctor_view import *

urlpatterns= [
    path('create/',DoctorCreateView.as_view(),name='doctor-create'),
    path('<int:pk>/update/',DoctorUpdateView.as_view(),name='doctor-update'),
    path('<int:pk>/delete/',DoctorDeleteView.as_view(),name='doctor-delete'),
    path('<int:pk>/detail/',DoctorDetailView.as_view(),name='doctor-detail'),
    path('list/',DoctorListView.as_view(),name='doctor-list'),
]
