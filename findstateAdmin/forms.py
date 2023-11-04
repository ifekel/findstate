from django import forms
from app.models import Property, PropertyReview, Agent
from users.models import CustomUser

class AgentForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}))
    properties = forms.ModelMultipleChoiceField(queryset=Property.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'id': 'properties'}))

    class Meta:
        model = Agent
        fields = ['name', 'image', 'properties']


class PropertyForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=300)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    rent_per_year = forms.DecimalField(max_digits=10, decimal_places=2)
    lot_area = forms.DecimalField(max_digits=10, decimal_places=2)
    floor_area = forms.DecimalField(max_digits=10, decimal_places=2)
    bed_rooms = forms.IntegerField()
    bath_rooms = forms.DecimalField(max_digits=10, decimal_places=2)
    garage = forms.IntegerField(max_value=10)
    year_build = forms.IntegerField()
    stories = forms.IntegerField()
    luggage = forms.BooleanField(required=False)
    water = forms.BooleanField(required=False)
    roofing = forms.Select(choices=['New', 'Old'])
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Property
        fields = ['name', 'address', 'description', 'price', 'rent_per_year', 'lot_area', 'floor_area', 'bed_rooms', 'bath_rooms', 'garage', 'year_build', 'stories', 'luggage', 'water', 'roofing', 'image']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    username = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(required=True, max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class PropertyReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}))
    property = forms.ModelChoiceField(queryset=Property.objects.all(), widget=forms.Select(attrs={'id': 'properties'}))
    review = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ratings = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PropertyReview
        fields = ['name', 'image', 'property', 'review', 'ratings']
