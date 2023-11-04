from django.urls import path
from .views import Home, About, Contact, Property, Properties, Service, Agent

app_name = 'app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact', Contact.as_view(), name='contact'),
    path('property/<uuid:pk>/', Property.as_view(), name='property'),
    path('properties/', Properties.as_view(), name='properties'),
    path('agent/', Agent.as_view(), name='agent'),
    path('services/', Service.as_view(), name='services'),
]
