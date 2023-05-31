from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from .models import Customer
from apps.products.utils import get_image


def customer_corr(request):
    df = pd.DataFrame(Customer.objects.all().values())
    corr = round(df["budget"].corr(df["employment"]), 2)

    plt.switch_backend("Agg")
    plt.figure(figsize=(12, 8))
    sns.jointplot(x="budget", y="employment", kind="reg", data=df).set_axis_labels(
        "Company Budget", "No of Employees"
    )
    graph = get_image()

    context = {"graph": graph, "corr": corr}

    return render(request, "customers/customers-index.html", context)
