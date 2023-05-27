import pandas as pd

from django.shortcuts import redirect, render
from apps.products.forms import PurchaseForm

from apps.products.models import Product, Purchase
from apps.products.utils import get_plot


def index(request):
    error_message = None
    df = None
    graph = None
    price = None

    products = Product.objects.all()
    products_df = pd.DataFrame(products.values())
    products_df["product_id"] = products_df["id"]

    purchases = Purchase.objects.all()
    purchases_df = pd.DataFrame(purchases.values())

    if purchases_df.shape[0] > 0:
        # merge
        df = (
            pd.merge(purchases_df, products_df, on="product_id")
            .drop(["id_y", "updated_at_y", "created_at_y"], axis=1)
            .drop(["updated_at_x"], axis=1)
            .rename({"id_x": "id", "created_at_x": "created_at"}, axis=1)
        )

        price = df["price"]

        if request.method == "POST":
            chart_type = request.POST.get("sales")
            date_from = request.POST.get("date_from")
            date_to = request.POST.get("date_to")

            print("chart_type: ", chart_type)

            df["created_at"] = df["created_at"].apply(lambda x: x.strftime("%Y-%m-%d"))
            df_group = df.groupby("created_at", as_index=False)["total_price"].agg(
                "sum"
            )

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = df[
                        (df["created_at"] > date_from) & (df["created_at"] < date_to)
                    ]
                    df_group = df.groupby("created_at", as_index=False)[
                        "total_price"
                    ].agg("sum")

                # function to get a graph
                graph = get_plot(
                    chart_type,
                    x=df_group["created_at"],
                    y=df_group["total_price"],
                    data=df,
                )

            else:
                error_message = "Please select a chart type to continue."

    else:
        error_message = "No records available."

    if df is not None:
        df = df.to_html()
    else:
        df = "<br>"

    context = {
        "error_message": error_message,
        # "products_df": products_df.to_html(),
        # "purchases_df": purchases_df.to_html(),
        # "df": df,
        "graph": graph,
        "price": price,
    }
    return render(request, "products/index.html", context)


def add_purchase(request):
    """
    handle purchase addition
    """
    form = PurchaseForm()

    if request.method == "POST":
        form = PurchaseForm(request.POST)

        if form.is_valid():
            new_purchased = form.save(commit=False)
            new_purchased.salesman = request.user
            new_purchased.save()
            return redirect("products__home")

    context = {"form": form}
    return render(request, "products/add.html", context)
