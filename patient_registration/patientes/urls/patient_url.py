from django.urls import path
from ..views.patient_view import *

urlpatterns = [
  path('create/',PatientCreateView.as_view(),name='patient-create'),
  path('<uuid:id>/update/',PatientUpdateView.as_view(),name='patient-update'),
  path('<uuid:id>/delete/',PatientDeleteView.as_view(),name='patient-delete'),
  path('<uuid:id>/detail/',PatientDetailView.as_view(),name='patient-detail'),
  path('list/',PatientListView.as_view(),name='patient-list'),
]
