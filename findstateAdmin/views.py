from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from app.models import Property, PropertyReview, Agent
from users.models import CustomUser
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from .decorators import prevent_authorized_access, admin_only
from .forms import AgentForm, PropertyForm, UserForm, PropertyReviewForm
from django.utils.decorators import method_decorator
import os
from dotenv import load_dotenv


load_dotenv()



@method_decorator(admin_only, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'findstateAdmin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class AddProperty(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'findstateAdmin/add-property.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class Property(UpdateView):
    model = Property
    context_object_name = 'property'
    form_class = PropertyForm
    template_name = 'findstateAdmin/property.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class AddReview(CreateView):
    model = PropertyReview
    form_class = PropertyReviewForm
    template_name = 'findstateAdmin/add-review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class Agents(TemplateView):
    template_name = 'findstateAdmin/agents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class AddAgent(CreateView):
    model = Agent
    form_class = AgentForm
    template_name = 'findstateAdmin/add_agents.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class Agent(DetailView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'findstateAdmin/agent_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


# Authentication routes
@method_decorator(prevent_authorized_access, name='dispatch')
class Login(LoginView):
    success_url = reverse_lazy('admin:dashboard')
    template_name = 'findstateAdmin/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context


class Logout(LogoutView):
    next_page = reverse_lazy('admin:login')


@method_decorator(prevent_authorized_access, name='dispatch')
class Register(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'findstateAdmin/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['APP_NAME'] = os.getenv('APP_NAME').title()
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        hashed_password = make_password(password)

        user = self.model.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=hashed_password, is_active=True, is_staff=True, is_superuser=True)
        user.save()
        return redirect(reverse('admin:login'))

    def form_invalid(self, form):
        print("Error")
        return redirect(reverse('admin:register'))