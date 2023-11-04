from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('properties/', Properties.as_view(), name='properties'),
    path('add-property/', AddProperty.as_view(), name='add_property'),
    path('property/<uuid:pk>/', Property.as_view(), name='property'),
    path('reviews/', Reviews.as_view(), name='reviews'),
    path('add-review/', AddProperty.as_view(), name='add_review'),
    path('agents/', Agents.as_view(), name='agents'),
    path('agents/<uuid:pk>/', Agent.as_view(), name='agent'),
    path('agents/add/', AddAgent.as_view(), name='add_agent'),
    path('users/', Users.as_view(), name='users'),
    path('users/<uuid:pk>/', User.as_view(), name='user'),
    path('users/add/<uuid:pk>/', AddUser.as_view(), name='add_user'),
    path('', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
]