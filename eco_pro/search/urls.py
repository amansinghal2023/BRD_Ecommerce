from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',SearchItems.as_view()),
    # path('item/',GetCartItem.as_view() ),
    # path('offer/',OfferAPI.as_view() ),
]