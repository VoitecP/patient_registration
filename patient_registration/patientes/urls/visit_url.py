from django.urls import path
from ..views.visit_view import *

urlpatterns = [
    path('create/',VisitCreateView.as_view(),name='visit-create'),
    path('<uuid:id>/update/',VisitUpdateView.as_view(),name='visit-update'),
    path('<uuid:id>/delete/',VisitDeleteView.as_view(),name='visit-delete'),
    path('<uuid:id>/detail/',VisitDetailView.as_view(),name='visit-detail'),
    path('list/',VisitListView.as_view(),name='visit-list'),
]
