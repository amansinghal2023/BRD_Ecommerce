from rest_framework import serializers
from .models import Profile,Address
from rest_framework import viewsets
from rest_framework import serializers
from authentication.models import Signup

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'profile', 'street_address', 'city', 'state', 'zip_code']

class ProfileSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id','first_name' ,'last_name' ,'email' ,'date_of_birth' ,'phone_number', 'addresses']