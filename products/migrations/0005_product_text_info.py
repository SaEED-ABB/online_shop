# Generated by Django 2.0.4 on 2018-04-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text_info',
            field=models.CharField(blank=True, max_length=2047),
        ),
    ]