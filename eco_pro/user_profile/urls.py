from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('user/',ProfileAPI.as_view() ),
    path('user/<int:pk>/',ProfileAPI.as_view() ),
    path('address/',AddressAPI.as_view() ),
    path('address/<int:pk>/',AddressAPI.as_view() ),
]