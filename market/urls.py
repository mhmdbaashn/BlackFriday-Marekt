from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.product, name='product'),
]