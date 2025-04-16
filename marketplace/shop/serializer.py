from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        """
        model - with which model linked serializer (Product)
        fields - include all fields of model "Product" in serializer
        """
        model = Product
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        """
        model - with which model linked serializer (Order)
        fields - include all fields of model "Order" in serializer
        """
        model = Order
        fields = "__all__"