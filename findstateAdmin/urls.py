from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('add-property/', AddProperty.as_view(), name='add_property'),
    path('property/<uuid:pk>/', Property.as_view(), name='property'),
    path('add-review/', AddReview.as_view(), name='add_review'),
    path('agents/', Agents.as_view(), name='agents'),
    path('agents/<uuid:pk>/', Agent.as_view(), name='agent'),
    path('agents/add/', AddAgent.as_view(), name='add_agent'),
    path('Oauth/login/', Login.as_view(), name='login'),
    path('Oauth/logout/', LogoutView.as_view(), name='logout'),
    path('Oauth/register/', Register.as_view(), name='register'),
]