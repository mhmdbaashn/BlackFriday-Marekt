from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product



@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    list_display = ('name', 'price', 'seller')
    search_fields = ['name']
    list_filter = ('price',)
    summernote_fields = ('description',)




