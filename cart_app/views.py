from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from product_app.models import Product
from .cart import Cart
from .forms import FormCart

def find_price(request):
    cart = Cart(request)
    return HttpResponse('Price total is ',cart.get_total_price())
def find_cart(request):
    product = get_object_or_404(Product,id=1)
    cart = FormCart()
    if product:
        return HttpResponse('product exist')
    else:
        return HttpResponse('product do not exist')
def cart_add(request,id1):
    if request.method == "POST":
        print("\n")
        cart = Cart(request)
        data = request.POST
        quantity = int(data['quantity'])
        b = Product.objects.get(id=id1)
        announce = cart.add(a=b, quantity=quantity)
        return redirect('shopping_cart')
def override_quantity(request,id2):
    if request.method == "POST":
        cart = Cart(request)
        data = request.POST
        print("\n")
        b = Product.objects.get(id=id2)
        print("ID of item to be updated : ",b)
        print("quantity : ",data['quantity'])
        quantity = int(data['quantity'])
        announce = cart.add(a=b,
                            quantity=quantity,
                            update_quantity=True)
        print("status : ")
        print(announce)
        return redirect('shopping_cart')
def shopping_cart(request):
    cart = Cart(request)
    form = FormCart()
    sum_prices = cart.get_total_price()
    return render(request,"shopping-cart.html",
                  {'product':cart,
                   'sum_prices':sum_prices,
                   'form':form})
def cart_remove(request, removed_id):
    if request.method == "POST":
        cart = Cart(request)
        product = get_object_or_404(Product, id=removed_id)
        cart.remove(product)
        return redirect('shopping_cart')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse('Cart has been cleared')

def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def checkout(request):
    cart = Cart(request)
    sum_price = cart.get_total_price()
    return render(request,"check-out.html",
                  {'product':cart,
                   'sum_price':sum_price})