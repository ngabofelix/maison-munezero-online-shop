from django import forms
from store.models import Product, ProductCategory

class CreteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'