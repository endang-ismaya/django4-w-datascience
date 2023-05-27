from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)
