# Generated by Django 4.1 on 2024-05-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_discount_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
