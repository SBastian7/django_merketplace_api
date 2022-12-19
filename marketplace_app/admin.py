from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.get_fields() if field.name not in ["id", "created_at", "updated_at", "listimages"]]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)