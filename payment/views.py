from django.shortcuts import render, redirect 
from cart.cart import Cart
from .forms import ShippingForm, ShippingAddress
from django.contrib import messages

def payment_success(request):
    return render(request, 'payment/payment_success.html', {})

def checkout(request):
    
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id = request.user.id)
        shipping_form = ShippingForm(request.POST or None ,instance=shipping_user)
        return render(request, 'payment/checkout.html', {'cart_products':cart_products, 'quantities':quantities, 'total':total, 'shipping_form':shipping_form})
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {'cart_products':cart_products, 'quantities':quantities, 'total':total, 'shipping_form':shipping_form})

def confirm_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()

        user_shipping = request.POST
        request.session['user_shipping'] = user_shipping

        
        return render(request, 'payment/confirm_order.html', {'cart_products':cart_products, 'quantities':quantities, 'total':total, 'shipping_info':user_shipping})
        

    else:
        messages.success(request, "دسترسی امکان پذیر نمیباشد")
        return redirect('home')
        
    