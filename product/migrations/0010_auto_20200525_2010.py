# Generated by Django 2.2.6 on 2020-05-25 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200525_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
