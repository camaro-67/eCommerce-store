# Generated by Django 3.0.8 on 2021-01-30 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0015_auto_20210130_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='p_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='p_latest_img',
        ),
    ]
