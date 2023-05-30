from django import forms
from apps.csvs.models import Csv


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ("file_name",)
