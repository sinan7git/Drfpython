# Generated by Django 3.2.6 on 2023-05-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='video',
        ),
    ]
