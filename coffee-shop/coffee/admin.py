from django.contrib import admin
from .models import Product, Category
# Register your models here.


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, CoffeeAdmin)
