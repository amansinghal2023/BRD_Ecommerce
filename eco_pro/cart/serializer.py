from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields="__all__"