from django import forms
from .models import Product

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),

             'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),

             'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-black-200'
            }),

             'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            })
        }