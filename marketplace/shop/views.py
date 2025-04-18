from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Order
from .serializer import ProductSerializer, OrderSerializer
from .permissions import IsAuthor
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category", lookup_expr="icontains")
    price_min = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["category", "price_min", "price_max"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthor]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def home(request):
    return render(request, "home.html")