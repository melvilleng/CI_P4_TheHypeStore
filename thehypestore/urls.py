"""thehypestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', product.views.index, name='show_product_route'),
    path('product/', product.views.all_product, name='show_allproduct_route'),
    path('product/create_product',product.views.create_product, name='create_product_route'),
    path('product/update_product/<product_id>',product.views.update_product, name='update_product_route'),
    path('product/delete_product/<product_id>',product.views.delete_product, name= 'delete_product_route'),
    path('cart/', include('cart.urls')),
    path('reviews/', include('reviews.urls')),
    path('product/product_details/<product_id>', product.views.product_details, name='product_details'),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('accounts.urls')),
]
