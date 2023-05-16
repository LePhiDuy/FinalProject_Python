import json

from django.http import JsonResponse
from coffee.models import Product
from cart.inherit import cartData
from django.shortcuts import render
from cart.models import *
# Create your views here.
def cart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    alerts = 'False'
    if not(request.user.is_authenticated):
        alerts = 'True'
    return render(request, "cart.html", {'items':items, 'order':order, 'cartItems':cartItems,'alert':alerts})

def checkout(request):
    if request.user.is_authenticated:
        data = cartData(request)
        items = data['items']
        order = data['order']
        cartItems = data['cartItems']
        total = order.get_cart_total
        if request.method == "POST":
            address = request.POST['address']
            city = request.POST['city']
            phone_number = request.POST['phone_number']
            payment = request.POST['payment']
            shipping_adress = CheckoutDetail.objects.create(address=address, city=city, phone_number=phone_number, customer=request.user.customer, total_amount=total, order=order, payment=payment)
            shipping_adress.save()
            if total == order.get_cart_total:
                order.complete = True
            order.save()
            id = order.id  
            alert = True
            return render(request, "checkout.html", {'alerts':alert, 'id':id})
        return render(request, "checkout.html", {'items':items, 'order':order, 'cartItems':cartItems, 'alert':False})
    else:
        data = cartData(request)
        items = data['items']
        order = data['order']
        cartItems = data['cartItems']
        alert = True
        return render(request, "cart.html", {'items':items, 'order':order, 'cartItems':cartItems,'alert':alert})
def updateItem(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    quantity = data['quantity']

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    update_order, created = UpdateOrder.objects.get_or_create(order_id=order, desc="Your Order is Successfully Placed.")

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + quantity)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - quantity)

    orderItem.save()
    update_order.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
