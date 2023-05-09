import json
from coffee.models import Product
from cart.models import *
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        for i in cart:
            try:
                cartItems += cart[i]["quantity"]

                product = Product.objects.get(id=i)
                print(product.price)
                total = (product.price * cart[i]["quantity"])

                order["get_cart_total"] += total
                order["get_cart_items"] += cart[i]["quantity"]

                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'image':product.image,
                    },
                    'quantity':cart[i]["quantity"],
                    'get_total':total
                }
                items.append(item)
            except:
                pass
        
    return {'cartItems':cartItems, 'items':items, 'order':order}