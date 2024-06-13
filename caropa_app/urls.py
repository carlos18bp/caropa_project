from django.urls import path
from caropa_app.views import product, home

urlpatterns = [
    path('products-data/', product.product_list, name='product-list'),
    path('home-data/', home.home_data, name="home-data"),
]