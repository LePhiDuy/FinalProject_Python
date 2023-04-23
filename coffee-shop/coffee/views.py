from .forms import *
from django.shortcuts import redirect, render, HttpResponse
from .models import Product, Category
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def home(request):
    selected_category = request.GET.get('category')
    categories = Category.objects.all()
    products = Product.objects.all()

    if selected_category:
        products = products.filter(category_id=selected_category)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': int(selected_category) if selected_category else None
    }

    return render(request, 'index.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
