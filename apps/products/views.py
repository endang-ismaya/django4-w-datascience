import pandas as pd

from django.shortcuts import render

from apps.products.models import Product, Purchase


def index(request):
    products = Product.objects.all()
    products_df = pd.DataFrame(products.values())
    products_df["product_id"] = products_df["id"]

    purchases = Purchase.objects.all()
    purchases_df = pd.DataFrame(purchases.values())

    # merge
    df = (
        pd.merge(purchases_df, products_df, on="product_id")
        .drop(["id_y", "updated_at_y", "created_at_y"], axis=1)
        .drop(["updated_at_x"], axis=1)
        .rename({"id_x": "id", "created_at_x": "created_at"}, axis=1)
    )

    context = {
        "products_df": products_df.to_html(),
        "purchases_df": purchases_df.to_html(),
        "df": df.to_html(),
    }
    return render(request, "products/index.html", context)
