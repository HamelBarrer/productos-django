from .models import Cart


def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    # obtener el valor del car id
    cart_id = request.session.get('cart_id')
    # Obtener el carrito de compras
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    # le colocamos un carrito a un usuario anonimo
    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart
