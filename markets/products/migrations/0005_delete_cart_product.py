# Generated by Django 3.2.5 on 2021-07-23 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210720_1948'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart_product',
        ),
    ]
