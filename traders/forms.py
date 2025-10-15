from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')
        widgets = {
			'name': forms.TextInput(attrs={
				'class': "form-control my-2"
			}),
   			'description': forms.Textarea(attrs={
				'class': "form-control mt-2"
			}),
            'price': forms.TextInput(attrs={
				'type': "number"
			})
		}
   
        labels = {
			'name': 'Product Name',
   			'description': 'Product Description',
            'price': 'Product Price'
		}

    def clean_name(self):
        
        name = self.cleaned_data['name']
        
        if (len(name.strip()) == 0):
            raise ValidationError("Product name cannot consist of only whitespace.")
        
        if (len(name) > 100):
            raise ValidationError("Product name must not be more than 100 characters.")

        return name
    
    def clean_description(self):
        
        description = self.cleaned_data['description']
        
        if (len(description.strip()) == 0):
            raise ValidationError("Product description cannot consist of only whitespace.")
        
        if (len(description) > 1000):
            raise ValidationError("Product description must not be more than 1000 characters.")

        return description
    
    def clean_price(self):
    
        price = self.cleaned_data['price']
        
        if price is not None and price <= 0:
            raise ValidationError("Product price can not be zero.")
        
        if price > 100.00:
            raise ValidationError("Product price should be less than $100.00")
        
        try:
            float(price)
        except ValueError:
            raise ValidationError("Please enter a valid number.")
        
        return price
