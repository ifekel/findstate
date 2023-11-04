from rest_framework import serializers
from app.models import Property, PropertyReview, Agent
from users.models import CustomUser

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'description', 'price', 'image', 'rent_per_year', 'lot_area', 'bed_rooms', 'bath_rooms', 'luggage', 'garage', 'floor_area', 'year_build', 'water', 'stories', 'roofing', 'timestamp']


class PropertyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyReview
        fields = ['id', 'property', 'name', 'review', 'ratings', 'timestamp']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'image', 'properties']
