# Generated by Django 3.2 on 2022-01-11 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='cutomer',
            new_name='customer',
        ),
    ]