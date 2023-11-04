from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Property, PropertyReview
import os
from dotenv import load_dotenv

load_dotenv()


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class Agent(TemplateView):
    template_name = 'agent.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class Contact(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class Service(TemplateView):
    template_name = 'services.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class Properties(TemplateView):
    template_name = 'properties.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

class Property(DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'property.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context



# Error handler Urls
def custom_error_404(request, e):
    context = {
        'APP_NAME': os.getenv('APP_NAME'),
    }
    return render(request, '404.html', context, status=404)

def custom_error_500(request):
    context = {
        'APP_NAME': os.getenv('APP_NAME'),
    }
    return render(request, '500.html', context, status=500)