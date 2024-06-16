from django.urls import path
from caropa_app.views import product, home, sale

urlpatterns = [
    path('products-data/', product.product_list, name='product-list'),
    path('home-data/', home.home_data, name="home-data"),
    path('create-sale/', sale.create_sale, name='create-sale'),
]