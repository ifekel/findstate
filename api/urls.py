from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('properties', PropertyViewSet, basename='properties'),

router.register('reviews', PropertyReviewViewSet, basename='property_reviews'),

router.register('users', UserViewSet, basename='users'),

router.register('agents', AgentViewSet, basename='agents'),

urlpatterns = router.urls