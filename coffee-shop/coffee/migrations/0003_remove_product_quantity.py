# Generated by Django 4.2 on 2023-05-17 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_rename_category_id_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]