from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = "__all__"

    
