from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=100)
    
    description = models.CharField(
        max_length=1000, 
        default=''
    )
    
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2, 
        default=0.0
    )
