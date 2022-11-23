from django.urls import path
from ..views.patient_view import *

urlpatterns = [
  path('create/',PatientCreateView.as_view(),name='patient-create'),
  path('<int:pk>/update/',PatientUpdateView.as_view(),name='patient-update'),
  path('<int:pk>/delete/',PatientDeleteView.as_view(),name='patient-delete'),
  path('<int:pk>/detail/',PatientDetailView.as_view(),name='patient-detail'),
  path('list/',PatientListView.as_view(),name='patient-list'),
]
