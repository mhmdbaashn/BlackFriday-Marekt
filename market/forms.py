from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Form that includes all required fields from the Product model.
    """
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'discount_price', 'stock', 'available', 'featured_image']
        
    # Validate that the regular price is not negative
    def clean_price(self):
        price = self.cleaned_data.get('price')
        print("Price entered:", price)  # Debugging
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    # Validate that the discount price is not negative
    def clean_discount_price(self):
        discount_price = self.cleaned_data.get('discount_price')
        if discount_price is not None and discount_price < 0:
            raise forms.ValidationError("Discount price cannot be negative.")
        return discount_price

    # Validate that the discount price is less than the regular price
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        discount_price = cleaned_data.get('discount_price')

        if price is not None and discount_price is not None:
            if discount_price >= price:
                self.add_error('discount_price', "Discount price must be less than the regular price.")
        
        return cleaned_data
