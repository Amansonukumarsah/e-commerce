# Generated by Django 4.0.5 on 2023-03-03 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='Category',
            field=models.CharField(choices=[('mb', 'mobile'), ('so', 'sofa'), ('ele', 'electronice'), ('Ts', 'T-Shirt'), ('by', 'Baby'), ('bg', 'Bags'), ('ft', 'Footwear')], default='null', max_length=100),
            preserve_default=False,
        ),
    ]