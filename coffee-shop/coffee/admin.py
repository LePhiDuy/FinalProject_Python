from django.contrib import admin
from .models import Product, Category
# Register your models here.


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


admin.site.register(Product, CoffeeAdmin)
