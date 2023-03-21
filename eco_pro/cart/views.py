from django.shortcuts import render ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import Signup
from product.models import Product
from .models import Cart
from .serializer import CartSerializer


class CartItems(APIView):
    def post(self,request):
        '''
        step 1- get product id and count 
        step 2 - store this in cart table 
        step 3- create a get method and get id whos user login by request.user.id
        step 4 - fetch all the item from cart db with the login user
        step 5- total item = add the total count all the product
        step 6- product.id.prize*count (total prize)
        '''
        user_id=request.user.id
        data= request.data
        print("---------------->.........",data)
        print("---------------->.........",user_id)

        # product_id = request.GET.get('id')
        # email= request.GET.get('email')

        # email_obj= Signup.objects.filter(email=email)
        # print(email_obj)
        # if len(email_obj)==0:
        #     return Response({"status":400,"error" : True, "messasge":"Invalid User"})
        # else:

        #     cart_obj= Cart(user=email_obj[0],product=[product_id])
        #     cart_obj.save()
        #     return Response({"status":200,"error" : False, "messasge":"Item has been added in cart"})

        # cart_obj= Cart(user=email,product=[product_id])
        # cart_obj.save()
        # return Response({"status":200,"error" : False, "messasge":"Item has been added in cart"})

        
    
        
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