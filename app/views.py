from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Property, PropertyReview


class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Agent(TemplateView    ):
    template_name = 'agent.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Service(TemplateView):
    template_name = 'services.html'

class Properties(TemplateView):
    template_name = 'properties.html'

class Property(DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'property.html'
