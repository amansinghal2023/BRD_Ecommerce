from rest_framework import serializers
from .models import Profile,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    # address1=AddressSerializer(many=True,read_only=True)
    # class Meta:
    #     model = Profile
    #     fields = ('id','first_name','last_name','email','phone_number','date_of_birth','address1')  

