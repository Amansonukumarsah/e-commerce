# Generated by Django 4.0.5 on 2023-02-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.CharField(choices=[('mb', 'mobile'), ('so', 'sofa'), ('ele', 'electronice'), ('Ts', 'T-Shirt'), ('by', 'Baby'), ('bg', 'Bags'), ('ft', 'Footwear')], max_length=100),
        ),
    ]