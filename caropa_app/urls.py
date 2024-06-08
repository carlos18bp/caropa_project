from django.urls import path
from caropa_app.views import product

urlpatterns = [
    path('api/products/', product.product_list, name='product-list'),
]