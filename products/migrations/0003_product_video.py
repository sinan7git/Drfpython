# Generated by Django 3.2.6 on 2023-05-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(null=True, upload_to='products/videos'),
        ),
    ]