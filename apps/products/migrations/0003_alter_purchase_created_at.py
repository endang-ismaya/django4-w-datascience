# Generated by Django 4.2.1 on 2023-05-27 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_purchase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
