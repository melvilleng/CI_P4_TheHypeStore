# Generated by Django 2.2.6 on 2020-05-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200525_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='sizes',
            field=models.CharField(choices=[('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra-Large')], max_length=150),
        ),
    ]
