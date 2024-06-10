from django.urls import path
from caropa_app.views import product

urlpatterns = [
    path('products/', product.product_list, name='product-list'),
]