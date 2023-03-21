from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import Product
from .serializer import ProductSerializer
from product.models import Category,Product
class SearchItems(APIView):
    serializer_class = ProductSerializer
    def get(self, request):
        search_param = request.GET.get('name')

        # queryset = Product.objects.all()

        queryset = Product.objects.all()
        if search_param:
            queryset = queryset.filter(Q(product_name__icontains=search_param) | Q(product_category__name__icontains=search_param))

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
