from .forms import *
from django.shortcuts import redirect, render, HttpResponse
from .models import Product
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
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
       return render(request,'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('/')
