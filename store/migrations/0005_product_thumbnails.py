# Generated by Django 4.2.5 on 2023-09-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_status_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnails',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images/thumbnails'),
        ),
    ]
