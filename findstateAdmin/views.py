from django.shortcuts import render, redirect, reverse
from app.models import Property, PropertyReview, Agent
from users.models import CustomUser
from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from .decorators import prevent_authorized_access, admin_only
from .forms import AgentForm
from django.utils.decorators import method_decorator



@method_decorator(admin_only('admin:login'), name='dispatch')
class Dashboard(TemplateView):
    template_name = 'findstateAdmin/dashboard.html'


class Properties(TemplateView):
    template_name = 'findstateAdmin/properties.html'


class AddProperty(CreateView):
    model = Property
    fields = ['name', 'address', 'description', 'price', 'rent_per_year', 'lot_area', 'bed_rooms',
              'bath_rooms', 'luggage', 'garage', 'floor_area', 'year_build', 'water', 'stories', 'roofing']
    template_name = 'findstateAdmin/add-property.html'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        address = form.cleaned_data['address']
        description = form.cleaned_data['description']
        price = form.cleaned_data['price']
        rent_per_year = form.cleaned_data['rent_per_year']
        lot_area = form.cleaned_data['lot_area']
        bed_rooms = form.cleaned_data['bed_rooms']
        bath_rooms = form.cleaned_data['bath_rooms']
        luggage = form.cleaned_data['luggage']
        garage = form.cleaned_data['garage']
        floor_area = form.cleaned_data['floor_area']
        year_build = form.cleaned_data['year_build']
        water = form.cleaned_data['water']
        stories = form.cleaned_data['stories']
        roofing = form.cleaned_data['roofing']
        image = self.request.POST.get('image')
        property = self.model.objects.create(
            name=name,
            address=address,
            description=description,
            price=price,
            rent_per_year=rent_per_year,
            lot_area=lot_area,
            bed_rooms=bed_rooms,
            bath_rooms=bath_rooms,
            luggage=luggage,
            garage=garage,
            floor_area=floor_area,
            year_build=year_build,
            water=water,
            stories=stories,
            roofing=roofing,
            image= image
        )

        property.save()

        return redirect(reverse('admin:properties'))


class Property(TemplateView):
    template_name = 'findstateAdmin/reviews.html'


class Reviews(TemplateView):
    template_name = 'findstateAdmin/reviews.html'


class AddReview(TemplateView):
    template_name = 'findstateAdmin/add-review.html'


class Agents(TemplateView):
    template_name = 'findstateAdmin/agents.html'


class AddAgent(CreateView):
    model = Agent
    form_class = AgentForm
    template_name = 'findstateAdmin/add_agents.html'


class Agent(DetailView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'findstateAdmin/agent_detail.html'


class Users(TemplateView):
    template_name = 'findstateAdmin/users.html'


class User(DetailView):
    model = CustomUser
    template_name = 'findstateAdmin/user_detail.html'
    context_object_name = 'user'


class AddUser(CreateView):
    model = CustomUser
    template_name = 'findstateAdmin/add_user.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'password', 'is_staff', 'is_superuser']

# Authentication routes

@method_decorator(prevent_authorized_access, name='dispatch')
class Login(LoginView):
    template_name = 'findstateAdmin/login.html'


class Logout(LogoutView):
    template_name = 'findstateAdmin/logout.html'


class Register(TemplateView):
    template_name = 'findstateAdmin/register.html'
