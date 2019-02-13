from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin (admin.ModelAdmin):
    fields = ( 'name', 'price', 'category', 'image' )
    list_display = ( 'name', 'price', 'category', 'image' )
    list_filter = ('category',)
    list_editable = ('price',)

admin.site.register(Product, ProductAdmin)