from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib import messages


def home(request):
    # Render the home page.
    return render(request, 'market/home_page.html')

@login_required
def product_list(request):
    # Display a list of all products (login required).
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})

def product_detail(request, pk):
    # Display details for a specific product.
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'market/product_detail.html', {'product': product})

@login_required
def product_create(request):
    """
    Handles the creation of a new product by the logged-in user.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'market/product_form.html', {'form': form})

def product_update(request, pk):
    """
    Allows the product seller to update their product. 
    Redirects with an error if the user is not the seller. 
    """    
    product = get_object_or_404(Product, pk=pk)
    if product.seller != request.user:
        messages.error(request, "You are not allowed to modify this product.")
        return redirect('product_list') 
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'market/product_form.html',  {'form': form, 'product': product})



@login_required
def product_delete(request, pk):
    """
    Deletes a product if the user is its seller; otherwise, shows an error and redirects.
    """
    product = get_object_or_404(Product, pk=pk)
    if product.seller != request.user:
        messages.error(request, "You are not allowed to delete this product.")
        return redirect('product_list') 
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'market/product_delete.html', {'product': product})