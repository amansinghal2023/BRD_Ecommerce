from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  SignupSerializer
from .models import Signup
from .service import validate_password,user_validation
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken

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
        
    def get(self, request, format=None):
        signup = Signup.objects.all()
        serializer = SignupSerializer(signup, many=True)
        print(serializer.data)
        return Response(serializer.data)

class LoginAPI(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        # print("---------------------------...............",email)
        # print("---------------------------...............",password)
        # flag=user_validation(email,password)
        # if flag==True:
        #     return Response({"status":200,"error" : False, "messasge":"login successfully"})
        # else:
        #     return Response({"status":400,"error" : True,"messasge":"not matching"})
        user=Signup.objects.get(email=email,password=password)
        username=Signup.objects.values_list('username', flat=True)
        print("--------------------------------->>>>",username[0])
        if user:
            refresh=RefreshToken.for_user(user)
            print(refresh)
            return Response({"status":200,
                             "username": str(username[0]),
                             "refresh":str(refresh),
                             "access":str(refresh.access_token)
                             })
        return Response({"status":404})
 