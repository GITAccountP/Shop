from django.contrib import admin

# Register your models here.
from .import models

class TradersAdmin(admin.ModelAdmin):
    list_display=('name',)
    

admin.site.register(models.Product, TradersAdmin)