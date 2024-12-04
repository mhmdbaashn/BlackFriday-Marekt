from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Category



@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    list_display = ('name', 'price', 'seller', 'category', 'stock' )
    search_fields = ['name']
    list_filter = ('price','stock')
    summernote_fields = ('description',)





admin.site.register(Category)
