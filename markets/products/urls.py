from django.urls import path, include
from .views import index, product, cart, add_cart

urlpatterns = [
    path('', index, name='products'),
    path('<int:product_id>', product, name='product'),
    path('cart/', cart, name='cart'),
    path('add_cart/<int:product_id>', add_cart, name='add_cart'),
]