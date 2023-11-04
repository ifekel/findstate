from django.shortcuts import render
from rest_framework import viewsets
from app.models import Property, PropertyReview, Agent
from .serializers import PropertySerializer, PropertyReviewSerializer, UserSerializer, AgentSerializer
from users.models import CustomUser
from rest_framework import permissions

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('?')
    serializer_class = PropertySerializer
    reviews = 'PropertyReviewViewSet'


class PropertyReviewViewSet(viewsets.ModelViewSet):
    queryset = PropertyReview.objects.all()
    serializer_class = PropertyReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

