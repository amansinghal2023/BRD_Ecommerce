from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',CartItems.as_view() ),
    path('item/',GetCartItem.as_view() ),
    path('delete/', CartItemDelete.as_view()),
    # path('offer/',OfferAPI.as_view() ),
]

# from django.urls import path
# from .views import CartItemDetailView

# urlpatterns = [
#     path('cart-items/<int:cart_item_id>/', CartItemDetailView.as_view()),
# ]