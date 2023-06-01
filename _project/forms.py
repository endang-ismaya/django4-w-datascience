from typing import Any, Dict
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=220)
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)

    def clean(self) -> Dict[str, Any]:
        data = self.cleaned_data

        username = data.get("username")
        password = data.get("password")

        # logic for custom validation

        return data
