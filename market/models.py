from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    # The 'Category' model represents a product category in the database

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    # The 'Product' model represents a product in the store

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
