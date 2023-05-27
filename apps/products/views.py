import pandas as pd

from django.shortcuts import render

from apps.products.models import Product, Purchase


def index(request):
    products = Product.objects.all()
    products_pd = pd.DataFrame(products.values())

    purchases = Purchase.objects.all()
    purchases_pd = pd.DataFrame(purchases.values())
    context = {
        "products_pd": products_pd.to_html(),
        "purchases_pd": purchases_pd.to_html(),
    }
    return render(request, "products/index.html", context)
