from django.contrib import admin
from .models import Car,Customer,Rent

# Register your models here.

class CustomerAdmin (admin.ModelAdmin):
    fields = ( 'firstname', 'lastname', 'dob', 'tel' )
    list_display = ( 'id','firstname', 'lastname', 'dob', 'tel' )
    list_filter = ('dob',)
    list_editable = ('firstname', 'lastname', 'dob', 'tel')

admin.site.register(Customer, CustomerAdmin)

class CarAdmin (admin.ModelAdmin):
    fields = ('name', 'brand', 'purchasing_date', 'price' )
    list_display = ('name', 'brand', 'purchasing_date', 'price' )
    list_filter = ('brand', 'purchasing_date', 'price' )
    list_editable = ('brand', 'purchasing_date', 'price')

admin.site.register(Car, CarAdmin)

class RentAdmin (admin.ModelAdmin):
    fields = ('start', 'stop', 'cost', 'customer', 'car')
    list_display = ('id', 'start', 'stop', 'cost', 'customer', 'car')
    list_filter = ('start', 'stop', 'cost', 'customer', 'car')
    list_editable = ('start', 'stop', 'cost', 'customer', 'car')

admin.site.register(Rent, RentAdmin)