from django.urls import path
from ..views.category_view import *

urlpatterns= [
    path('create/',CategoryCreateView.as_view(),name='category-create'),
    path('<uuid:id>/update/',CategoryUpdateView.as_view(),name='category-update'),
    path('<uuid:id>/delete/',CategoryDeleteView.as_view(),name='category-delete'),
    path('<uuid:id>/detail/',CategoryDetailView.as_view(),name='category-detail'),
    path('list/',CategoryListView.as_view(),name='category-list'),
]