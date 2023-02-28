from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  SignupSerializer
from .models import Signup
from .service import validate_password,user_validation


class SignupAPI(APIView):
    def post(self, request):
        serializer=SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print("----------",serializer.data)
        flag = validate_password(request.data.get('password'),request.data.get('c_password'))
        print(flag)
        if flag == True:
            serializer.save()
            return Response({"status":200,"error" : False, "messasge":"Data is saved successfully"})
        else:
            return Response({"status":400,"error" : True,"messasge":"password and confirm password is not same"})
        
class LoginAPI(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
        flag=user_validation(email,password)

        if flag==True:
            return Response({"status":200,"error" : False, "messasge":"login successfully"})
        else:
            return Response({"status":400,"error" : True,"messasge":"not matching"})