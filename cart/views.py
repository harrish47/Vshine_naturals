from django.shortcuts import render, redirect
from products.models import Products
from .models import Cart, CartItem


def add_to_cart(request, product_id):
    
    product = Products.objects.get(id=product_id) 
    try:    
        cart = Cart.objects.get(user=request.user)    
    except Cart.DoesNotExist:    
        cart = Cart.objects.create(user=request.user)
        cart.save()
    
    try: 
        cartItem = CartItem.objects.get(product=product, cart=cart)
        cartItem.quantity += 1
        cartItem.save()
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,
        )
        cartItem.save()
    return redirect('cart:cart')

def view_cart(request):
    cart = Cart.objects.get(user=request.user) 
    cartItem = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cartItem)
    context = {
        'cart': cart,
        'cart_items': cartItem,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

def remove_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart')
        
