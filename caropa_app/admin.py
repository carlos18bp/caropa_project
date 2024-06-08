from django.contrib import admin
from .models import Product, ProductDetail, Category, Size, Color, ProductByRef
from .forms import ProductForm
from django_attachments.admin import AttachmentsAdminMixin

admin.site.site_header = "Caropa Project"
admin.site.site_title = "Caropa Project"
admin.site.index_title = "Welcome to Caropa Project Control Panel"

class ProductAdmin(AttachmentsAdminMixin, admin.ModelAdmin):
	form = ProductForm

	def delete_queryset(self, request, queryset):
		for obj in queryset:
			obj.delete()


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductByRef)