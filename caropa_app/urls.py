from django.urls import path
from caropa_app.views import product, home, category

urlpatterns = [
    path('products/', product.product_list, name='product-list'),
    path('home-data/', home.home_data, name="home-data"),
    path('categories/', category.category_list, name="category-list"),
]