from rest_framework import serializers
from app.models import Property, PropertyReview, Agent
from users.models import CustomUser
from django.utils import formats


class PropertyReviewSerializer(serializers.ModelSerializer):
    formatted_timestamp = serializers.SerializerMethodField()

    class Meta:
        model = PropertyReview
        fields = ['id', 'property', 'image', 'name', 'review', 'ratings', 'formatted_timestamp']

    def get_formatted_timestamp(self, obj):
        return formats.date_format(obj.timestamp, "F j, Y")


class PropertySerializer(serializers.ModelSerializer):
    reviews = PropertyReviewSerializer(many=True)
    
    class Meta:
        model = Property
        fields = ['id', 'name', 'address', 'description', 'price', 'image', 'rent_per_year', 'lot_area', 'bed_rooms', 'bath_rooms', 'luggage', 'garage', 'floor_area', 'year_build', 'water', 'stories', 'roofing', 'reviews', 'timestamp']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'image', 'properties']
