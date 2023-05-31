from django.urls import path
from apps.products import views

urlpatterns = [
    path("", views.index, name="products__home"),
    path("statistics/", views.statistics, name="products__statistics"),
    path("add/", views.add_purchase, name="products__add_purchase"),
    path("sales/", views.sales_dist, name="products__sales"),
]
