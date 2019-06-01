from django.contrib import admin

# Register your models here.
from core.models import Product


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
