# Generated by Django 4.1.7 on 2023-03-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0009_sight_timing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='kids_price',
            new_name='kid_price',
        ),
    ]