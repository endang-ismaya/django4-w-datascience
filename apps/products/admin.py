from django.contrib import admin

from apps.products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


admin.site.register(Product, ProductAdmin)
