from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

# class OfferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Offer
#         fields = "__all__"

    
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields="__all__"


