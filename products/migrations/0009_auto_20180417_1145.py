# Generated by Django 2.0.4 on 2018-04-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
