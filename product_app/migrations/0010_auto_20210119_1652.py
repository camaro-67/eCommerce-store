# Generated by Django 3.0.8 on 2021-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0009_auto_20210119_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
