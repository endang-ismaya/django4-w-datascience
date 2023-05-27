from django.contrib import admin

from apps.products.models import Product, Purchase


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "price",
        "quantity",
        "total_price",
        "salesman",
        "created_at",
    )
    exclude = ("total_price",)
    list_editable = ("created_at",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
