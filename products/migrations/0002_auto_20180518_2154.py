# Generated by Django 2.0.4 on 2018-05-18 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setproduct',
            name='basket',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='set_products', to='products.Basket'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setproduct',
            name='product',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='set_product', to='products.Product'),
            preserve_default=False,
        ),
    ]