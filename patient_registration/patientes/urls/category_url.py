from django.urls import path
from ..views.category_view import *

urlpatterns= [
    path('create/',CategoryCreateView.as_view(),name='category-create'),
    path('<int:pk>/update/',CategoryUpdateView.as_view(),name='category-update'),
    path('<int:pk>/delete/',CategoryDeleteView.as_view(),name='category-delete'),
    path('<int:pk>/detail/',CategoryDetailView.as_view(),name='category-detail'),
    path('list/',CategoryListView.as_view(),name='category-list'),
]