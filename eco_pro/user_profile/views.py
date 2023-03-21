from django.shortcuts import render
# Create your views here.
from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  ProfileSerializer,AddressSerializer
from .models import Profile,Address
from .service import getprofile
from rest_framework.permissions import IsAuthenticated
from authentication.models import Signup

from rest_framework import viewsets

class ProfileAPI(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self, request):
        user_id=request.user.id
        data= request.data
        print("---------------->.........",data)
        print("---------------->.........",user_id)
        data['signup_profile']=user_id
        # print("------------------------>>>>>>>>>>>>>>>>>.",data)
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
        
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        data=getprofile(serializer.data)
        print("This is the data ------------->",data)
        return Response({"status" : 200 , "error" : False , "data":data})

class AddressAPI(APIView):
    def post(self, request):
        user_id=request.user.id
        data= request.data
        print("---------------->.........",data)
        print("---------------->.........",user_id)
        data['profile']=user_id
        print("------------------------->",request.data)
        serializer=AddressSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        # serializer.save()
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
    

