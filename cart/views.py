from django.shortcuts import render, get_object_or_404,redirect,reverse
from product.models import Product
from django.contrib import messages

# Create your views here.
def add_to_cart(request, product_id):

    #open file find the key 'shopping cart' in the session
    #if 'shopping cart' is not found return empty dict
    cart = request.session.get('shopping_cart', {})

    
    #The product not in the cart
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': 99,
            'qty': 1,
        }
        messages.success(request, f"Product:{product.name} has been added")

    #product already in cart
    else:
        cart[product_id]['qty'] += 1
    
    #save the session
    request.session['shopping_cart'] = cart
    return redirect(reverse('show_product_route'))

def show_cart(request):
    #Get the session
    cart = request.session.get('shopping_cart')
    return render(request, 'cart/show_cart.template.html',{
        'cart': cart
    })