from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
# Create your views here.

def list_product(request, category_slug = None):
    category = None
    products = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'products/list_product.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        category = get_object_or_404(Category, slug=category_slug)
        product_detail = Product.objects.get(category = category, slug = product_slug)
    except Exception as e:
        raise e
    context = {
        'product': product_detail
    }
    return render(request, 'products/product_detail.html', context)