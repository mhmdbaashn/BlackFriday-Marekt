from django import forms
from .models import Product




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'discount_price', 'stock', 'available', 'seller', 'featured_image']
