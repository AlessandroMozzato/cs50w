# Generated by Django 2.0.3 on 2018-12-01 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181201_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price_big',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
