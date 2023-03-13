from django.shortcuts import render
# Create your views here.
from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  ProfileSerializer,AddressSerializer
from .models import Profile,Address
from .service import getprofile
# from .service import validate_password,user_validation
# from .models import Category,Product
# # Create your views here.
from rest_framework import viewsets

class ProfileAPI(APIView):
    def post(self, request):
        serializer=ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"error" : False, "messasge":"Data is saved successfully"})
    

    
    def get(self, request, format=None,pk=None):
        id=pk
        if id is not None:
            profile=Profile.objects.get(id=id)
            serializer = ProfileSerializer(profile)
            return Response({"status" : 200 , "error" : False , "data":serializer.data})
        
        personal = Profile.objects.all()
        serializer = ProfileSerializer(personal, many=True)
        # print(serializer.data)
        data=getprofile(serializer.data)
        # print("THE FULL DATA IS RESPONSE -------------------->",data[0])
        return Response(data)

class AddressAPI(APIView):
    def post(self, request):
        serializer=AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"error" : False, "messasge":"Data is saved successfully"})
    

    def get(self, request, format=None,pk=None):
        id=pk
        if id is not None:
            add=Address.objects.get(id=id)
            serializer = AddressSerializer(add)
            return Response({"status" : 200 , "error" : False , "data":serializer.data})
        
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        print(serializer.data)
        return Response(serializer.data)