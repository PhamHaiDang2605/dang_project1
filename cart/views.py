from django.shortcuts import render

# Create your views here.
from .models import Cart, CartItem

def cart_detail(request):
    cart = Cart.objects.first()  # Giả sử chỉ có 1 giỏ hàng
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'items': items})
