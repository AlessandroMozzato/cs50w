# Generated by Django 2.0.3 on 2018-11-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('num_toppings', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30, null=True)),
                ('price', models.IntegerField()),
                ('price_big', models.IntegerField(null=True)),
            ],
        ),
    ]
