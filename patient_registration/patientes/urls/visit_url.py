from django.urls import path
from ..views.visit_view import *

urlpatterns = [
    path('create/',VisitCreateView.as_view(),name='visit-create'),
    path('<int:pk>/update/',VisitUpdateView.as_view(),name='visit-update'),
    path('<int:pk>/delete/',VisitDeleteView.as_view(),name='visit-delete'),
    path('<int:pk>/detail/',VisitDetailView.as_view(),name='visit-detail'),
    path('list/',VisitListView.as_view(),name='visit-list'),
]
