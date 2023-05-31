from django.urls import path
from apps.customers import views

urlpatterns = [
    path("", views.customer_corr, name="customers__home"),
]
