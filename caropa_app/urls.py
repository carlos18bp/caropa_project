from django.urls import path
from caropa_app.views import product, home, create_order, capture_order

urlpatterns = [
    path('products-data/', product.product_list, name='product-list'),
    path('home-data/', home.home_data, name="home-data"),
    path('create-order/', create_order.create_order, name='create-order'),
    path('capture-order/', capture_order.capture_order, name='capture-order'),
]