# Generated by Django 4.0.5 on 2023-03-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_reviews_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]