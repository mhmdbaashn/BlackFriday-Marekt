from django import forms
from .models import Product, Review

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),  # The rating field will be handled via JavaScript
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment here...'}),
        }
    
    # You can add validation if needed
    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get('rating')
        comment = cleaned_data.get('comment')

        if not rating or not comment:
            raise forms.ValidationError("Both rating and comment are required.")

        if rating not in range(1, 6):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        
        return cleaned_data