# Generated by Django 4.2.13 on 2024-07-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0012_product_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
