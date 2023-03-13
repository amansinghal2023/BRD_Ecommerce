from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  CategorySerializer,ProductSerializer
# from .models import Signup
# from .service import validate_password,user_validation
from .models import Category,Product
from .service import getcategory
# getcategorybyid
# # Create your views here.
class CategoryAPI(APIView):
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"error" : False, "messasge":"Data is saved successfully"})
    
    def get(self, request, format=None,pk=None):
        print("query param is",request.GET.get('id'))
        id=pk
        if id is not None:
            cat=Category.objects.get(id=id)
            serializer = CategorySerializer(cat)
            # data=getcategorybyid(serializer.data)
            return Response({"status" : 200 , "error" : False , "data":serializer.data})
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        response_list = []
        for data in serializer.data:
            response_dict={}
            response_dict["category"] = data["name"]
            response_dict["product_details"] = data["category"]
            response_list.append(response_dict)
            # print("----------------------",i)
            

        # print("------------",serializer.data[0])
    
        return Response({"status":200, "data": response_list})

class ProductAPI(APIView):
    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":200,"error" : False, "messasge":"Data is saved successfully"})
    
    def get(self, request, format=None,pk=None):
        id=pk
        # print(id)
        if id is not None:
            product=Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            # data=getcategorybyid(serializer.data)
            return Response({"status" : 200 , "error" : False , "data":serializer.data})

        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        data=getcategory(serializer.data)
        print(data)
        return Response({"status" : 200 , "error" : False , "data":data})
    
    def put(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        instance=Product.objects.get(id=pk)
        serializer=ProductSerializer(instance=instance,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data})
        else:
            # return Response( {"error":serializer.errors}, status=status.HTTP_400_ BAD_REQUEST)
            return Response( {"error":serializer.errors})
        
    def patch(self,request,pk,*args,**kwargs):
        id=pk
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,data=request.data,partial=True)

        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response({"data":serializer.data})
        else:
            # return Response( {"error":serializer.errors}, status=status.HTTP_400_ BAD_REQUEST)
            return Response( {"error":serializer.errors})
        
class ProductDetailsView(APIView):
    def get(self, request):
        id = request.GET.get('id')
        product_details = Product.objects.filter(id = id).values_list('product_details')
        print("----------------------->",product_details)
        return Response({
            "status":200,
            "product_details":product_details[0][0]
        })
    
    # product = Product.objects.all()
    #     serializer = ProductSerializer(product, many=True)
    #     data=getcategory(serializer.data)
    #     print(data)
    #     return Response({"status" : 200 , "error" : False , "data":data})
        