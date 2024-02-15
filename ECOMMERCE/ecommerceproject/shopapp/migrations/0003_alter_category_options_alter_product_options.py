# Generated by Django 4.2.9 on 2024-02-06 06:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0002_alter_category_options_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
    ]