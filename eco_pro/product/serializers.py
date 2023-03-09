from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    category=ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('id','name','category')        
        # fields = "__all__"


