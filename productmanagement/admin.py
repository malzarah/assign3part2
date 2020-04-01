from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Customer, Product


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city','state','zip','notes']
    model = Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_manufacturer']
    model = Product



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)