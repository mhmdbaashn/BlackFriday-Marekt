from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ProductForm
from django.contrib import messages
from .forms import ReviewForm

def home(request):
    # Eport 4 Product to homepage
    featured_products = Product.objects.all()[:4]
    return render(request, 'market/home_page.html', {'featured_products': featured_products})

@login_required
def product_list(request):
    # Display a list of all products (login required).
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ReviewForm()
    rating_range = range(1, 6)  # Rating range from 1 to 5

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('product_detail', pk=product.pk)  # Reload the page after submission
    
    return render(request, 'market/product_detail.html', {
        'product': product,
        'form': form,
        'rating_range': rating_range,
    })

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
            product.save()  # save product after adding seller
            # messages success
            messages.success(request, "The product has been successfully added!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'market/product_form.html', {'form': form})


@login_required
def product_update(request, pk):
    """
    Allows the product seller or admin to update the product.
    Redirects with an error if the user is not the seller or an admin.
    """
    product = get_object_or_404(Product, pk=pk)
    
    if product.seller != request.user and not request.user.is_superuser:
        messages.error(request, "You are not allowed to modify this product.")
        return redirect('product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "The product has been successfully updated!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'market/product_form.html', {'form': form, 'product': product})

@login_required
def product_delete(request, pk):
    """
    Deletes a product if the user is its seller or an admin; otherwise,
    shows an error and redirects.
    """
    product = get_object_or_404(Product, pk=pk)
    
    if product.seller != request.user and not request.user.is_superuser:
        messages.error(request, "You are not allowed to delete this product.")
        return redirect('product_list')
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, "The product has been deleted successfully.")
        return redirect('product_list')
    
    return render(request, 'market/product_delete.html', {'product': product})

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the user has already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        messages.error(request, 'You have already reviewed this product.')
        return redirect('product_detail', pk=product.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        # Check if rating and comment are provided
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if not rating or not comment:  # If either field is missing
            messages.error(request, 'Both rating and comment are required.')
            return redirect('product_detail', pk=product.id)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been submitted successfully!')
            return redirect('product_detail', pk=product.id)

    else:
        form = ReviewForm()

    return render(request, 'market/product_detail.html', {
        'product': product,
        'form': form,
    })