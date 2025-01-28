from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category, Review




@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    list_display = ('name', 'price', 'seller', 'category', 'stock' )
    search_fields = ['name']
    list_filter = ('price','stock')
    summernote_fields = ('description',)





admin.site.register(Category)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ['product__name', 'user__username']
