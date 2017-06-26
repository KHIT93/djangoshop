from django.contrib import admin
from .models.product import Product
from .models.category import Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "price", "description", "inventory", "created_at", "category"]
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "created_at"]
    class Meta:
        model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
