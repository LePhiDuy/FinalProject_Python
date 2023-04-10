from django.shortcuts import render, HttpResponse
from .models import Product
from django.http import JsonResponse
# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})
