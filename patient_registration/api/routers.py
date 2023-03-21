from django.urls import path, include
from .viewsets import *
from rest_framework.routers import DefaultRouter 
from rest_framework_nested.routers import NestedDefaultRouter


router=DefaultRouter()
router.register('patientes', PatientViewSet, basename='router-patientes')
router.register('visits', VisitViewSet, basename='router-visits')
router.register('doctors', DoctorViewSet, basename='router-doctors')
router.register('categories', CategoryViewSet, basename='router-categories' )


nested_router=NestedDefaultRouter
# opinion_router=routers.NestedDefaultRouter(router, "doctors", lookup="opinion_pk" )
# opinion_router.register("opinions",OpinionViewSet, basename="doctor-opinion")

# urlpatterns = router.urls
