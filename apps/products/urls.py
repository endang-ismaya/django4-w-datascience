from django.urls import path
from apps.products import views

urlpatterns = [
    path("", views.index, name="products__home"),
    path("add/", views.add_purchase, name="products__add_purchase"),
]
