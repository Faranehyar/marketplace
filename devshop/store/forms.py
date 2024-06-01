from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
        }