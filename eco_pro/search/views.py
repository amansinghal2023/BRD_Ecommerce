from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Category,Product

# Create your views here.
class SearchItems(APIView):
    def get(self,request):
        search_item= request.GET.get('name')
        print("------------------------------",search_item)
        # search_obj= Product.objects.filter(product_name=search_item)
        search_obj= Product.objects.filter(product_name__icontains=search_item)
        print("-----------------",search_obj[0])
        # print("-----------------",search_obj[0])
        product = list(Product.objects.filter(product_name__icontains=search_obj[0]).values())

        return Response({"status":200,"error" : False, "product" : product})
