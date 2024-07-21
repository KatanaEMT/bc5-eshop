from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'qty',
            'category',
            'guarantee',
            'expiration_date'
        ]