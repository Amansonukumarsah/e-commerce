# Generated by Django 4.0.5 on 2023-05-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0011_alter_product_category_alter_reviews_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]