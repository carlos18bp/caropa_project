from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    Product, ProductDetail, Category, Size, Color, Home, HomeCategory, Banner, Sale, SoldProduct
)
from .forms import ProductForm, HomeForm
from django_attachments.admin import AttachmentsAdminMixin

class ProductAdmin(AttachmentsAdminMixin, admin.ModelAdmin):
    form = ProductForm

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

class HomeAdmin(AttachmentsAdminMixin, admin.ModelAdmin):
    form = HomeForm

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

class SaleAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for sale in queryset:
            sale.delete()

# Custom AdminSite to organize models by sections
class CaropaAdminSite(admin.AdminSite):
    site_header = 'Caropa Project'
    site_title = 'Caropa Project'
    index_title = 'Welcome to Caropa Project Control Panel'

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        # Custom structure for the admin index
        custom_app_list = [
            {
                'name': _('Home Management'),
                'app_label': 'home_management',
                'models': [
                    model for model in app_dict.get('caropa_app', {}).get('models', [])
                    if model['object_name'] in ['Home', 'HomeCategory', 'Banner']
                ]
            },
            {
                'name': _('Product Management'),
                'app_label': 'product_management',
                'models': [
                    model for model in app_dict.get('caropa_app', {}).get('models', [])
                    if model['object_name'] in ['Product', 'ProductDetail', 'Category', 'Size', 'Color']
                ]
            },
            {
                'name': _('Sales Management'),
                'app_label': 'sales_management',
                'models': [
                    model for model in app_dict.get('caropa_app', {}).get('models', [])
                    if model['object_name'] in ['Sale', 'SoldProduct']
                ]
            }
        ]
        return custom_app_list

# Create an instance of the custom AdminSite
admin_site = CaropaAdminSite(name='myadmin')

# Register models with the custom AdminSite
admin_site.register(Home, HomeAdmin)
admin_site.register(HomeCategory)
admin_site.register(Banner)
admin_site.register(Product, ProductAdmin)
admin_site.register(ProductDetail)
admin_site.register(Category)
admin_site.register(Size)
admin_site.register(Color)
admin_site.register(Sale, SaleAdmin)
admin_site.register(SoldProduct)
