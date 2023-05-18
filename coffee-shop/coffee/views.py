from django.shortcuts import get_object_or_404, render, redirect

from cart.inherit import cartData
from .models import Product
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def list_product(request, category_slug = None):
    category = None
    products = None
    data = cartData(request)
    cartItems = data['cartItems']
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all()
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': page_products,
        'product_count': product_count,
        'cartItems': cartItems,
    }
    return render(request, 'products/list_product.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        category = get_object_or_404(Category, slug=category_slug)
        product_detail = Product.objects.get(category = category, slug = product_slug)
    except Exception as e:
        raise e
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'product': product_detail,
        'cartItems': cartItems,
    }
    return render(request, 'products/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(name__icontains=keyword)
            product_count = products.count()
        else:
            return redirect('home')
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'products/list_product.html', context)