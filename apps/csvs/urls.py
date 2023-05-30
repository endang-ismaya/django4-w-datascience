from django.urls import path
from apps.csvs import views

urlpatterns = [
    path("", views.upload_file, name="csvs__upload"),
]
