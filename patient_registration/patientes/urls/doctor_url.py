from django.urls import path
from ..views.doctor_view import *

urlpatterns= [
    path('create/',DoctorCreateView.as_view(),name='doctor-create'),
    path('<uuid:id>/update/',DoctorUpdateView.as_view(),name='doctor-update'),
    path('<uuid:id>/delete/',DoctorDeleteView.as_view(),name='doctor-delete'),
    path('<uuid:id>/detail/',DoctorDetailView.as_view(),name='doctor-detail'),
    path('list/',DoctorListView.as_view(),name='doctor-list'),
]
