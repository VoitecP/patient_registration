from django.urls import path
from ..views.summary_view import *

urlpatterns = [
    path('',SummaryListView.as_view(),name='summary'),
]
