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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', blank=True, null=True)

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum([review.rating for review in reviews]) / reviews.count()
        return 0

    def review_count(self):
        return self.reviews.count()

    def __str__(self):
        return self.name

class Review(models.Model):
    # Rating option
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.rating} Stars"

    class Meta:
        constraints = []    
        