from django import forms
from django_attachments.models import Library
from .models import Home, Product

class ProductForm(forms.ModelForm):
    """
    Form for the Product model.

    This form handles the creation and updating of Product instances, ensuring that
    a gallery is associated with the product.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set the gallery field as not required.
        """
        super().__init__(*args, **kwargs)
        self.fields['gallery'].required = False

    def save(self, commit=True):
        """
        Save the Product instance, ensuring that a gallery is associated with it.

        Args:
            commit (bool): Whether to commit the changes to the database.

        Returns:
            Product: The saved Product instance.
        """
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
    """
    Form for the Home model.

    This form handles the creation and updating of Home instances, ensuring that
    galleries are associated with the carousel presentation and section 3.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set the carousel_presentation and section_3_gallery fields as not required.
        """
        super().__init__(*args, **kwargs)
        self.fields['carousel_presentation'].required = False
        self.fields['section_3_gallery'].required = False

    def save(self, commit=True):
        """
        Save the Home instance, ensuring that galleries are associated with the carousel presentation and section 3.

        Args:
            commit (bool): Whether to commit the changes to the database.

        Returns:
            Home: The saved Home instance.
        """
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
