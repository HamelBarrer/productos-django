from django.shortcuts import render, redirect, get_object_or_404

from .models import CardProducts
from products.models import Product

from .utils import get_or_create_cart


def cart(request):
    template_name = 'carts/cart.html'
    cart = get_or_create_cart(request)

    return render(request, template_name, {
        'cart': cart,
    })


def add(request):
    template_name = 'carts/add.html'
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    # cart.products.add(product, through_defaults={
    #     'quantity': quantity,
    # })

    cart_product = CardProducts.objects.create_or_update_quantity(
        cart=cart, product=product, quantity=quantity)

    return render(request, template_name, {
        'quantity': quantity,
        'cart_product': cart_product,
        'product': product,
    })


def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')
