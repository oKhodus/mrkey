from django.contrib import admin
from .models import Product, Order, Category, Review, ShippingInfo

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'created_at', 'is_paid')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ShippingInfo)