# Generated by Django 4.0.5 on 2023-03-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_alter_reviews_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='Rat',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
