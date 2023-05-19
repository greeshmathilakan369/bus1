from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

#1 serializer for customer
class customer_serializer(serializers.ModelSerializer):
    class Meta:
        model=Customer_details
        fields="__all__"

#2 serializer for bus list
class buslist_seriializer(serializers.ModelSerializer):
    class Meta:
        model=Bus_list
        fields="__all__"
#3 serializer for reservation
class reservation_serializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations
        fields="__all__"  
#4) serializer for price
class Booking_serializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"          
