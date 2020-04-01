from django import forms
from .models import Customer, Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','city','state','zip','notes')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','product_manufacturer','product_price','product_available_status','product_Supplier')