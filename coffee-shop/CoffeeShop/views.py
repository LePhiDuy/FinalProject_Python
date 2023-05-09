from django.shortcuts import render
from cart.models import Customer
from coffee.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import createuserform
from cart.inherit import cartData
from django.contrib.auth.models import User
def home(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request, 'index.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        # form=createuserform()
        # if request.method=='POST':
        #     print(0)
        #     form=createuserform(request.POST)
        #     pass1=request.POST['password1']
        #     pass2=request.POST['password2']
        #     error = 0
        #     if pass1 != pass2:
        #         error += 1
        #         messages.error(request, "Passwords do not match",'danger')
        #         return redirect('register')
            
        #     if form.is_valid() :
        #         print(1)
        #         user=form.save()
        #         print(2)
        #         messages.success(request, "Registration successful, please log in",'success')
        #         return redirect('login')
        #     else:
        #         print(3)
        #         messages.error(request, "Invalid username or password",'danger')
        #         return redirect('register')
        # context = {
        #     'form': form,
        # }
        if request.method=="POST":   
            username = request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            if password1 != password2:
                alert = True
                return render(request, "register.html", {'alert':alert})
            
            user = User.objects.create_user(username=username, password=password1, email=email)
            customers = Customer.objects.create(user=user, name=first_name+last_name, phone_number=phone_number, email=email)
            user.save()
            customers.save()
            messages.success(request, "Registration successful, please log in",'success')
            return redirect('login')
        return render(request, 'register.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context={}
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password",'danger')
                return render(request,'login.html',context)
        return render(request,'login.html',context)
    
def logoutPage(request):
    logout(request)
    return redirect('/')