from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('category/<int:pk>/',CategoryAPI.as_view() ),
    path('category/',CategoryAPI.as_view() ),
    path('product/',ProductAPI.as_view() ),
    path('product/<int:pk>/',ProductAPI.as_view() ),
    path('product/details/',ProductDetailsView.as_view()),
    # path('offer/',OfferAPI.as_view() ),
]