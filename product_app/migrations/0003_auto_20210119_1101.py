# Generated by Django 3.0.8 on 2021-01-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_auto_20210115_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='p_desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='p_made_in',
        ),
        migrations.AddField(
            model_name='product',
            name='p_name',
            field=models.CharField(default=True, max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='p_price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
    ]
