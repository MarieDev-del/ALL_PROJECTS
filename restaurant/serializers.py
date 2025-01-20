from rest_framework import serializers
from .models import Booking

# Define a serializer for the Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Serialize all fields in the model
