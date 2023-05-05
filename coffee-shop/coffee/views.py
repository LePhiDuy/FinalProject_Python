from .forms import *
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Product, Category
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            pass1=request.POST['password1']
            pass2=request.POST['password2']
            error = 0
            if pass1 != pass2:
                error += 1
                messages.error(request, "Passwords do not match",'danger')
                return redirect('register')
            
            if form.is_valid() :
                user=form.save()
                messages.success(request, "Registration successful, please log in",'success')
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       messages.error(request, "Invalid username or password",'danger')
       return render(request,'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('/')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})