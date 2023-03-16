from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Cart
from product.models import Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"
