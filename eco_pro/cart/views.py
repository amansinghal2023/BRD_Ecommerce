from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import Signup
from product.models import Product
from .models import Cart
from .serializer import CartSerializer


class CartItems(APIView):
    def get(self,request):
        product_id = request.GET.get('id')
        email= request.GET.get('email')

        # email_obj= Signup.objects.filter(email=email)
        # print(email_obj)
        # if len(email_obj)==0:
        #     return Response({"status":400,"error" : True, "messasge":"Invalid User"})
        # else:
        cart_obj= Cart(user=email,product=[product_id])
        cart_obj.save()
        return Response({"status":200,"error" : False, "messasge":"Item has been added in cart"})
        
    
        
class GetCartItem(APIView):
    def get(self,request):
        email= request.GET.get('email')

        cart_obj= list(Cart.objects.filter(user=email).values())
        # cart_obj= Cart.objects.get(user_id= email_obj[0])
        # print("-----------------",cart_obj)
        # product = list(Product.objects.filter(id = cart_obj.product[0]).values())

        return Response({"status":200,"error" : False, "product" : cart_obj})

class CartItemDelete(APIView):
    """
    Delete a cart item.
    """
    def delete(self, request):
        product_id = request.GET.get('id')
        email= request.GET.get('email')

        print("???????????????????????",product_id)

        email_obj= Cart.objects.filter(user=email)

        print("------------------------------------>",email_obj)
        print(email_obj)
        if len(email_obj)==0:
            return Response({"status":400,"error" : True, "messasge":"Invalid User"})
        else:
            cart_obj= Cart.objects.filter(user=email_obj[0],product=[product_id])
            # cart_obj= Cart.objects.get(user_id= email_obj[0])

            print("----------------<<<<<<",cart_obj)
            cart_obj.delete()
            return Response({"status":200,"error" : False, "messasge":"Item has been Deleted From The cart"})