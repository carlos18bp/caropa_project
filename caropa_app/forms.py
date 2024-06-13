from django import forms
from django_attachments.models import Library
from .models import Product, Home

class ProductForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['gallery'].required = False

	def save(self, commit=True):
		obj = super().save(commit=False)
		if not hasattr(obj, 'gallery'):
			lib = Library()
			lib.save()
			obj.gallery = lib
		if commit:
			obj.save()
		return obj

	class Meta:
		model = Product
		fields = '__all__'

class HomeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['carousel_presentation'].required = False
        self.fields['section_3_gallery'].required = False

    def save(self, commit=True):
        obj = super().save(commit=False)
        if not hasattr(obj, 'carousel_presentation'):
            lib = Library()
            lib.save()
            obj.carousel_presentation = lib
        if not hasattr(obj, 'section_3_gallery'):
            lib = Library()
            lib.save()
            obj.section_3_gallery = lib
        if commit:
            obj.save()
        return obj

    class Meta:
        model = Home
        fields = '__all__'