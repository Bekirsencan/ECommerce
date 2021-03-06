from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from store.models import Product

def cart_summary(request):
    return render(request, 'store/cart/summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int (request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_quantity)
        response = JsonResponse({'qty': product_quantity})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int(request.POST.get('productqty'))
        cart.update(product=product_id, product_qty=product_quantity)
        response = JsonResponse({'Success':True})
        return response