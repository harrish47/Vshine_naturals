from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from .models import *

def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        'orders.html',
        {'orders': orders}
    )

def place_order(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        status="Pending"
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect('order:my_orders')