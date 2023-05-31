"""
Project URLs
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from _project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("products/", include("apps.products.urls"), name="products"),
    path("upload/", include("apps.csvs.urls")),
    path("customers/", include("apps.customers.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
